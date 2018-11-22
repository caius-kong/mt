数据来源：
src-train.txt ==> not_extract_en.txt                 |           src-train.txt ==> not_extract_xx.txt
src-val.txt ==> extract_en.txt (0-5000)              |           src-val.txt ==> extract_xx.txt (0-5000)
src-test.txt ==> extract_en.txt (5001 - 10000)       |           src-test.txt ==> extract_xx.txt (5001 - 10000)


备注：目前抽取脚本还不够完善，因此验证文本 与 测试文本 需要手动检查一遍，去掉不优秀的句子（例如js、css）