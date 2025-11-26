<h1 style="font-family: '仿宋', 'FangSong', 'Times New Roman', serif; color: orange; font-size: 2em; font-weight: bold; text-align: center; border-bottom: none; margin-bottom: 0;">MNN 测试流程</h1>
<p style="font-family: 'Times New Roman', serif; font-size: 1em; text-align: right; margin-top: 0;">Livia Tassel</p>
<div style="font-family: 'Times New Roman', 'FangSong', '仿宋', serif;">

[TOC]

# 模型下载
MNN 官方的 llmexport.py 脚本无法识别 Meta 官方的原始权重模型，所以必须先下载与 Hugging Face transformers 库兼容的模型权重。首选 Hugging Face [官方源](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)，不过下载 Llama 系列模型需要提前在官网申请并通过认证。

如果因为网络等问题无法在官网下载，也可以选择在国内镜像 ModelScope 上下载（选择已经被转换为 Hugging Face 格式的模型）。
Llama 2 (7B): https://huggingface.co/meta-llama/Llama-2-7b-chat-hf
Llama 3 (8B): https://modelscope.cn/models/Undi95/Meta-Llama-3-8B-hf

模型下载可以参考以下脚本（注意修改文件路径）：
```python
import os
from modelscope.hub.snapshot_download import snapshot_download

model_id = "Undi95/Meta-Llama-3-8B-hf"
model_name = model_id.split('/')[-1]

base_download_dir = "/home10T/ljq/MNN/models"
local_dir = os.path.join(base_download_dir, model_name)

# cache_path = "/home10T/.cache/modelscope_hub" 
cache_path = "/home10T/ljq/.cache/modelscope_hub"

print(f"from ModelScope download: {model_id}")
print(f"to: {local_dir}")

snapshot_download(
    model_id=model_id,
    revision='master',
    cache_dir=cache_path,
    local_dir=local_dir,
)

print(f"Successful download to: {local_dir}!")
```

# 模型转换
## 环境
在 MNN 源码目录下，新建 Conda 环境并安装所有依赖。
```bash
conda create -n mnn python=3.10
conda activate mnn
cd ./MNN/transformers/llm/export
pip install -r requirements.txt
```

## 执行转换
```bash
python llmexport.py \
    --path /path/to/models \
    --export mnn \
    --hqq \
    --quant_bit 4 \
    --dst_path /path/to/converted models
```
成功执行脚本后，将在 dst_path 目录下生成完整的 MNN 模型文件，目录应包含以下文件：
```bash
.
└── model
     ├── config.json
     ├── embeddings_bf16.bin
     ├── llm.mnn
     ├── llm.mnn.json
     ├── llm.mnn.weight
     ├── onnx/
          ├──llm.onnx
           ├──llm.onnx.data
     ├── llm_config.json
     └── tokenizer.txt
```

# 模型部署
将模型文件夹从服务器下载到本地，手机端打开“开发者选项”并启用“USB 调试”（不同品牌手机进入“开发者选项”的方式不同，请自行搜索）。

本机执行以下命令推送模型至手机端：
```bash
adb shell mkdir -p /data/local/tmp/mnn_models
adb push ~/path/to/mnn_model /data/local/tmp/mnn_models/
```
推送成功后，mnn 模型应出现在 App 的模型列表中。

# 模型测试
## 模型编译
在 MNN 根目录下：
```bash
mkdir build_linux && cd build_linux
cmake .. -DMNN_BUILD_LLM=true \
         -DMNN_AVX512=true \
         -DCMAKE_INSTALL_PREFIX=./install
make -j16
make install
```
- -DMNN_BUILD_LLM=true：加入 Attention 等算子（必须）。
- -DMNN_AVX512=truex86：Mac/Linux 可利用 AVX512 指令集加速。
- -DCMAKE_INSTALL_PREFIX=./install：将库文件安装到 `./MNN/build_linux/install` 目录下。

编译完成后，会在 `./build_linux/install` 目录下生成核心库文件（如 libMNN.so，libllm.so）。

## 模型测试
为了避免污染 MNN 源代码，可以在其同级目录下创建测试文件夹 MNNT 和 sentencepiece（用于在测试代码中分词），以及对应的编译环境，最终的文件结构如下（仅供参考）：
```bash
.
├── MNN/                                     # MNN 仓库
│   ├── build_linux/
│   │   ├── install/
│   │   │   ├── lib/
│   │   │   │   ├── libMNN.so
│   │   │   │   └── libMNN_Express.so
│   │   │   └── include/
│   │   └── ...
│   ├── source/
│   ├── include/
│   └── ...
|
├── MNNT/
│   ├── build_linux/                         # MNNT 编译目录
│   │   └── llm_precision_test               # 可执行文件
│   ├── llm_precision.cpp                    # 测试代码
│   ├── CMakeList.txt
│   └── datasets                             # 测试集 
│ 
|
└── sentencepiece/                           # SentencePiece 仓库
    └── build_linux/
        └── src/
            └── libsentencepiece.a / libsentencepiece.so
```
同样地，为 SentencePiece 编译库文件：
```bash
cd /home10T/ljq/sentencepiece/build_linux
cmake ..
make -j16
```

然后就可以 MNNT 目录下编写测试代码（llm_precision.cpp），测试代码中调用 MNN 模型接口进行推理，以下是以 `WMT14 EN→DE` 测试集为例编写的测试代码示例：
```cpp
double run_wmt_test(Llm* llm, const std::vector<std::string>& prompts, int max_token_number, int run_index) {
    std::string hyp_filename = "wmt_run_" + std::to_string(run_index) + ".txt";
    std::ofstream ofp_hyp(hyp_filename);
    if (!ofp_hyp.is_open()) {
        MNN_ERROR("Failed to open BLEU output file: %s\n", hyp_filename.c_str());
    }

    int prompt_len = 0;
    int decode_len = 0;
    int64_t prefill_time_us = 0;
    int64_t decode_time_us = 0; 
    
    int64_t total_ttft_us = 0;
    int64_t total_tpot_us = 0;
    int valid_requests = 0;

    auto context = llm->getContext();

    for (int i = 0; i < prompts.size(); i++) {
        std::string original_prompt = prompts[i];

        // if (original_prompt.substr(0, 1) == "#" || original_prompt.empty()) {
        //     continue;
        // }

        std::string instruction_prompt = "Please translate the following English text into German, without explanation or annotation, simply output the German text directly:\n" + original_prompt;
        valid_requests++;

        auto time_req_start = std::chrono::high_resolution_clock::now();
        llm->response(instruction_prompt, nullptr, nullptr, 0);
        llm->generate(1);
        auto time_first_token = std::chrono::high_resolution_clock::now();
        total_ttft_us += std::chrono::duration_cast<std::chrono::microseconds>(time_first_token - time_req_start).count();

        llm->generate(1);
        auto time_second_token = std::chrono::high_resolution_clock::now();
        total_tpot_us += std::chrono::duration_cast<std::chrono::microseconds>(time_second_token - time_first_token).count();

        llm->reset(); 
        
        std::ostringstream bleu_output_stream;
        
        if (max_token_number > 0) {
            std::string config_str = "{\"max_new_tokens\":" + std::to_string(max_token_number) + "}";
            llm->set_config(config_str.c_str());
        }

        llm->response(instruction_prompt, &bleu_output_stream); 

        std::string raw_output = bleu_output_stream.str();
        std::string line_output = sanitize_for_tsv(raw_output);
        ofp_hyp << line_output << std::endl;
        
        prompt_len += context->prompt_len;
        decode_len += context->gen_seq_len;
        prefill_time_us += context->prefill_us;
        decode_time_us += context->decode_us;
        
        llm->reset(); 
    }
    ofp_hyp.close();

    float prefill_s = prefill_time_us / 1e6;
    float decode_s = decode_time_us / 1e6;
    double avg_ttft_ms = (valid_requests > 0) ? (double)total_ttft_us / valid_requests / 1000.0 : 0.0;
    double avg_tpot_ms = (valid_requests > 0) ? (double)total_tpot_us / valid_requests / 1000.0 : 0.0;

    printf("\n--- Run %d WMT/Benchmark Report ---\n", run_index);
    printf("BLEU hypotheses saved to: %s\n", hyp_filename.c_str());
    printf("Avg TTFT (Manual): %.2f ms\n", avg_ttft_ms);
    printf("Avg Token Latency (Manual): %.2f ms/token\n", avg_tpot_ms);
    printf("----------------------------------\n");
    printf("Total Prompts = %d\n", valid_requests);
    printf("Prompt Tokens = %d \n", prompt_len);
    printf("Decode Tokens = %d \n", decode_len);
    printf("Prefill Time  = %.2f s \n", prefill_s);
    printf("Decode Time   = %.2f s \n", decode_s);
    if (prefill_s > 0) printf("Prefill Speed = %.2f tok/s \n", prompt_len / prefill_s);
    if (decode_s > 0) printf("Decode Speed  = %.2f tok/s \n", decode_len / decode_s);
    printf("----------------------------------\n");
    return avg_ttft_ms;
}
```
推理核心为 `llm->response(instruction_prompt, nullptr, nullptr, 0);` 和 `llm->generate(1);` 两个函数。 

测试代码编写完成后，将下载好的测试集与测试代码至于同一目录下，编译链接 MNN 与 SentencePiece 库文件，可以参考以下 CMakeLists.txt 文件：
```bash
cmake_minimum_required(VERSION 3.10)
project(MNNPrecisionTest_Linux CXX)

message(STATUS "MNN Lib Path: /home10T/ljq/MNN/build_linux")
message(STATUS "MNN Source Path: /home10T/ljq/MNN")
message(STATUS "Tokenizer Lib Path: /home10T/ljq/sentencepiece/build_linux/")

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
  message(STATUS "Build type not set, defaulting to 'Release'")
endif()

link_directories(/home10T/ljq/MNN/build_linux) 
link_directories(/home10T/ljq/sentencepiece/build_linux//src) 

include_directories(
    /home10T/ljq/MNN/transformers/llm/engine/include
    /home10T/ljq/MNN/include
    /home10T/ljq/MNN/tools
    /home10T/ljq/MNN/3rd_party
    /home10T/ljq/sentencepiece/src
    /home10T/ljq/MNN/source
    /home10T/ljq/MNN/3rd_party/half
)

file(GLOB_RECURSE LLM_ENGINE_SRC
    /home10T/ljq/MNN/transformers/llm/engine/src/*.cpp
    /home10T/ljq/MNN/transformers/llm/engine/src/speculative_decoding/*.cpp
)

add_executable(llm_precision_test
    llm_precision.cpp
    ${LLM_ENGINE_SRC}
)

target_link_libraries(llm_precision_test
    PRIVATE
    /home10T/ljq/MNN/build_linux/install/lib/libMNN.so
    /home10T/ljq/MNN/build_linux/install/lib/libMNN_Express.so
    /home10T/ljq/sentencepiece/build_linux/src/libsentencepiece.so
    pthread
    dl
)

message(STATUS "CMake configuration done. Run 'make' to build.")
```
※ 切记将以上文件中的 `/home10T/ljq/` 改为实际路径！！！

至此，MNNT 目录下应该至少有 llm_precision.cpp（测试文件），mmlu_test.csv（测试集）以及 CMakeList.txt 三个文件。然后，来到 `MNNT/build_linux` 目录下完成编译，得到可执行文件 llm_precision_test：
```bash
cd /home10T/ljq/MNNT/build_linux
cmake .. 
make -j16
ls -l llm_precision_test
```

最后，执行可执行文件完成测试：
```bash
cd ./MNNT/build_linux
./llm_precision_test /path/to/llama2_mnn/config.json \
                     /path/to/mmlu_test.csv \
                     mmlu
```