from fastchat.data_process import data_process
import nltk
import os

porter = nltk.PorterStemmer()


def common_word(doc_list, labels, labels_stemed):
    common_list = []
    doc_list_s = []
    pre_labels_list = []
    for i in range(len(doc_list)):
        num = 0
        pre_label_list = []
        # print(doc_list[i])
        tokens = doc_list[i].split()
        doc_list_s.append(' '.join(porter.stem(t) for t in tokens))
        for j in range(len(labels[i])):
            if labels[i][j] in doc_list[i] or labels_stemed[i][j] in doc_list_s[i]:
                num = num + 1
                print(doc_list[i])
                print(labels[i][j])
                pre_label_list.append(labels[i][j])
        # print("===========================================")
        common_list.append(num)
        pre_labels_list.append(pre_label_list)
    return common_list, pre_labels_list


# doc_list, labels,labels_stemed = data_process("../data//", "SemEval2010")
# for d in doc_list:
#     print(d)
# common_list,pre_labels_list=common_word(doc_list, labels,labels_stemed)
# print(common_list)
# print(pre_labels_list)
# pre_labels_list=[]
# with open('result/english/SemEval2010_sifrank_results10-0.86.txt', 'r', encoding='UTF-8-sig') as f:
#     for line in f.readlines():
#         label_list=line.replace('\n', '').replace('(', ',').replace(')', '').split(',')[:10]
#         pre_label_list = [i.strip() for i in label_list]
#         pre_labels_list.append(pre_label_list)
#         # pre_labels_list.append(pre_label_list)
# # print(pre_labels_list)
# word_count = [len(words.split(' ')) for sublist in pre_labels_list for words in sublist]
# print(word_count)
# average_words = sum(word_count) / len(word_count)
# print(average_words)

#
# from collections import Counter
# # 给定的列表
# # word_count = [2,2,2,3,3,1,5]
# # 使用Counter计算数字的出现次数
# counts = Counter(word_count)
#
# # 输出结果
# for number, count in counts.items():
#     print(f"数字 {number} 出现 {count} 次。")


# 计算候选词平均个数---英文
# label_lists=[]
# with open('result/english/keyphrase1030_2sifrank_results5-0.89.txt', 'r', encoding='UTF-8-sig') as f:
#     for line in f.readlines():
#         label_list=line.replace('\n', '').split(',')
#         label_lists.append(len(label_list))
#
# print(label_lists)
# print(sum(label_lists)/1030)

# 计算中文关键词的平均长度

# text_path = 'keyphrase1030/abstract_%d.txt'
# number = 1
# pre_labels_list = []
# while number <= 1030:
#     data = ''
#     if os.path.exists(text_path % number) is True:
#         with open(text_path % number, 'r', encoding='UTF-8-sig') as file:
#             text = file.readlines()
#             # print(text)
#             pre_label_list = text[1].replace('\n', '').split(' ')
#             pre_labels_list.append(pre_label_list)
#     number = number + 1
#
# print(pre_labels_list)
# word_count = [len(words.encode('gbk')) / 2 for sublist in pre_labels_list for words in sublist]
# print(word_count)
# average_words = sum(word_count) / len(word_count)
# print(average_words)

# 计算中文摘要的平均长度

text_path = 'keyphrase1030/abstract_%d.txt'
number = 1
pre_labels_list = []
while number <= 1030:
    data = ''
    if os.path.exists(text_path % number) is True:
        with open(text_path % number, 'r', encoding='UTF-8-sig') as file:
            text = file.readlines()
            # print(text)
            # pre_label_list = text[1].replace('\n', '').split(' ')
            pre_labels_list.append(text[0].replace('\n', ''))
    number = number + 1

print(pre_labels_list)
word_count = [len(words) / 2 for words in pre_labels_list]
print(len(word_count))
average_words = sum(word_count) / len(word_count)
print(average_words)
