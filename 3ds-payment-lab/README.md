# 3DS 支付原理安全实验

完全本地的教学模拟器，不连接真实银行、Visa、Mastercard 或真实支付网络。

## 运行

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate
pip install flask
python app.py
```

打开 `http://127.0.0.1:5000/`。

实验卡号：`4111 1111 1111 1111`

## 实验流程

1. 输入实验卡号并创建 USD 1,000 模拟交易。
2. 获取 transaction ID。
3. 打开“模拟银行 App”。
4. 输入 transaction ID。
5. 点击确认或拒绝，观察 `requires_action -> authorized/declined`。

真实支付系统通常涉及 Merchant、Payment Gateway、3DS Server、Card Network、Issuer ACS 和持卡人 Challenge。本项目把它们压缩成一个 Flask 服务，仅用于理解状态流转。

**安全边界：不接受真实银行卡数据、不发送真实 OTP、不连接真实支付 API、不模拟真实银行登录页面。**