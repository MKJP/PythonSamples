#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import re

###
# すべて「ひらがな」であればマッチする
###
pattern = u'^[\u3040-\u3098]+$'

# 対象の文字列もUnicodeにあわせる
string = u'あいうえお' # 正常系
result = re.match(pattern, string)
assert result is not None
print(result)
# <_sre.SRE_Match object at ...>が出力される

string = u'XあいうえおX' # 異常系、前後に対象外文字あり
result = re.match(pattern, string)
assert result is None
print(result)
# Noneが出力される

string = u'あいXうえお' # 異常系、途中に対象外文字あり
result = re.match(pattern, string)
assert result is None
print(result)
# Noneが出力される

###
# すべて「カタカナ」であればマッチする
###
pattern = u'^[\u30a1-\u30fa\u30fc]+$'

# 対象の文字列もUnicodeにあわせる
string = u'アイウエオ' # 正常系
result = re.match(pattern, string)
assert result is not None
print(result)
# <_sre.SRE_Match object at ...>が出力される

string = u'XアイウエオX' # 異常系、前後に対象外文字あり
result = re.match(pattern, string)
assert result is None
print(result)
# Noneが出力される

string = u'アイXウエオ' # 異常系、途中に対象外文字あり
result = re.match(pattern, string)
assert result is None
print(result)
# Noneが出力される

###
# すべて「漢字」であればマッチする
###
pattern = u'^[\u4e00-\u9fff]+$'

# 対象の文字列もUnicodeにあわせる
string = u'文字列' # 正常系
result = re.match(pattern, string)
assert result is not None
print(result)
# <_sre.SRE_Match object at ...>が出力される

string = u'X文字列X' # 異常系、前後に対象外文字あり
result = re.match(pattern, string)
assert result is None
print(result)
# Noneが出力される

string = u'文字X列' # 異常系、途中に対象外文字あり
result = re.match(pattern, string)
assert result is None
print(result)
# Noneが出力される

