import sys
import platform

print("=" * 40)
print("🚀 我的项目正在 GitHub Actions 中运行！")
print("=" * 40)
print(f"Python 版本: {sys.version}")
print(f"操作系统: {platform.system()} {platform.release()}")
print()

# 简单的功能演示
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("✅ 所有测试通过！")

test_add()