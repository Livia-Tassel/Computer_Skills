<h1 style="font-family: '仿宋', 'FangSong', 'Times New Roman', serif; color: orange; font-size: 2em; font-weight: bold; text-align: center; border-bottom: none; margin-bottom: 0;">PageAttention 入门</h1>
<p style="font-family: 'Times New Roman', serif; font-size: 1em; text-align: right; margin-top: 0;">Livia Tassel</p>
<div style="font-family: 'Times New Roman', 'FangSong', '仿宋', serif;">

[TOC]

---

# Batch
$Batch$ 指的是 GPU 在一次计算中同时处理的多个独立用户请求的集合。

简单来说，更大的 $batch\ size$ 意味着 GPU 可以一次性为更多的用户生成回复，从而最大化利用其强大的平行计算能力，提高整体服务的效率（吞吐量）。

原论文[^1]中提到，限制 GPU 内存的，不是模型权重，而是 $KV\ Cache$。因为，$KV\ Cache$ 是动态增长的，当模型为一个请求生成回复时，它会为每一个已经生成出来的 $token$ 计算并储存一组 $Key$（$K$） 和 $Value$（$V$） 向量。用户输入的句子越长，或模型生成的回复越长，这个请求对应的 $KV\ Cache$ 就越大。

在 $vLLM$ 出现之前，普遍采用静态批处理（$Static\ Batching$）。系统为了处理一个 $batch$，会预先分配一块连续的、巨大的内存空间给这个 $batch$ 中的每一个请求。这个空间的大小是按照可能的最长回复来计算的，然而大部分请求根本不会生成那么长的回复，导致预留的内存空间大量被闲置浪费（内存内部碎片化）。这些被浪费的内存，本可以用来容纳更多用户的请求。
![alt text](pageattention.assets/1.png)

# vLLM
<table>
<tr align="center">
    <td><img src="pageattention.assets/2.png" width="300"></td>
</tr>
<tr align="center">
    <td><em>vLLM</em></td>
</tr>
</table>


[^1]: [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://ar5iv.labs.arxiv.org/html/2309.06180)