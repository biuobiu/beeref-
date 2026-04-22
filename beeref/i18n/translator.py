# This file is part of BeeRef.
#
# BeeRef is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BeeRef is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BeeRef.  If not, see <https://www.gnu.org/licenses/>.

from .zh_CN import zh_CN


class Translator:
    """翻译器类，用于管理应用程序的多语言支持"""
    
    def __init__(self):
        self.translations = zh_CN
    
    def translate(self, text):
        """翻译文本"""
        return self.translations.get(text, text)


# 创建全局翻译器实例
translator = Translator()

# 为了方便使用，创建一个全局翻译函数
def _(text):
    return translator.translate(text)