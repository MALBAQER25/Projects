# مشروع لنظام تسجيل دخول للطالب محمد الباقر
# يتحقق من اسم المستخدم وكلمة المرور بثلاث محاولات فقط

acct = {
    "user": "mohammed",
    "pw": "12345678",
    "fullname": "Mohammed Al-Baqer",
    "age": 21,
    "email": "mohammed@mail.ru",
    "locked": False
}

MAX_TRIES = 3

def main():
    if acct.get("locked") or not acct.get("user"):
        print("الحساب مقفول أو بياناته غير متوفرة.")
        return

    for attempt in range(1, MAX_TRIES + 1):
        username = input("اكتب اسم المستخدم: ").strip()
        password = input("اكتب كلمة المرور: ").strip()

        if username == acct["user"] and password == acct["pw"]:
            print("\nتم تسجيل الدخول بنجاح. مرحباً بك!")
            print("معلومات الحساب:")
            print("  الاسم الكامل:", acct["fullname"])
            print("  العمر:", acct["age"])
            print("  الايميل:", acct["email"])
            print("  اسم المستخدم:", acct["user"])
            return
        else:
            remaining = MAX_TRIES - attempt
            if remaining > 0:
                print(f"خطأ في البيانات — تبقّى {remaining} محاولة.\n")
            else:
                acct.clear()
                acct["locked"] = True
                print("\nأخطأت ثلاث مرات. تم حذف بيانات الحساب وقفله.")
                return

if __name__ == "__main__":
    main()
