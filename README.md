```markdown
# URL Shortener API

این پروژه یک API RESTful برای کوتاه کردن URLهای طولانی با استفاده از Django و Django REST Framework است. این API شامل قابلیت‌هایی برای ایجاد، بازیابی، به‌روزرسانی و حذف URLهای کوتاه شده است. همچنین امکان مشاهده آمار تعداد دفعات دسترسی به URLهای کوتاه شده وجود دارد.

## ویژگی‌ها

- **ایجاد URL کوتاه**: کاربر می‌تواند با ارسال یک درخواست POST به `/api/shorten/`، یک URL طولانی را کوتاه کند.
- **تغییر مسیر**: کاربر با مراجعه به `/<short_url>/` به URL اصلی هدایت می‌شود و تعداد دفعات دسترسی افزایش می‌یابد.
- **دریافت آمار**: آمار مربوط به تعداد کلیک‌ها و اطلاعات مرتبط با URL کوتاه شده از طریق `/api/stats/<short_url>/` قابل دسترسی است.
- **به‌روزرسانی URL کوتاه**: امکان به‌روزرسانی URL اصلی مربوط به یک URL کوتاه شده.
- **حذف URL کوتاه**: امکان حذف یک URL کوتاه شده.

## مراحل نصب و راه‌اندازی

### پیش‌نیازها

- [Python 3.12](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)

### نصب

1. مخزن پروژه را کلون کنید:

   ```bash
   git clone git@github.com:IMAN-NEONSER/url-shortner.git
   cd url-shortener-api
   ```

2. یک محیط مجازی ایجاد و فعال کنید:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # برای ویندوز: venv\Scripts\activate
   ```

3. بسته‌های مورد نیاز را نصب کنید:

   ```bash
   pip install django djangorestframework
   ```

4. مایگریشن‌های پایگاه داده را اعمال کنید:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. سرور توسعه را اجرا کنید:

   ```bash
   python manage.py runserver
   ```

   API اکنون در `http://127.0.0.1:8000/` در دسترس است.

## استفاده از API

### 1. ایجاد URL کوتاه

- **Endpoint**: `/api/shorten/`
- **Method**: `POST`
- **Request Body**:

  ```json
  {
    "original_url": "https://example.com"
  }
  ```

- **Response**:

  ```json
  {
    "original_url": "https://example.com",
    "short_url": "abc123",
    "clicks": 0
  }
  ```

### 2. تغییر مسیر به URL اصلی

- **Endpoint**: `/<short_url>/`
- **Method**: `GET`

این درخواست کاربر را به URL اصلی هدایت می‌کند و تعداد دفعات دسترسی افزایش می‌یابد.

### 3. دریافت آمار

- **Endpoint**: `/api/stats/<short_url>/`
- **Method**: `GET`
- **Response**:

  ```json
  {
    "original_url": "https://example.com",
    "short_url": "abc123",
    "clicks": 42
  }
  ```

### 4. به‌روزرسانی URL کوتاه

- **Endpoint**: `/api/update/<short_url>/`
- **Method**: `PUT`
- **Request Body**:

  ```json
  {
    "original_url": "https://newexample.com"
  }
  ```

- **Response**:

  ```json
  {
    "original_url": "https://newexample.com",
    "short_url": "abc123",
    "clicks": 42
  }
  ```

### 5. حذف URL کوتاه

- **Endpoint**: `/api/delete/<short_url>/`
- **Method**: `DELETE`
- **Response**: `204 No Content`

## تست API

برای تست API می‌توانید از ابزارهایی مثل Postman یا Curl استفاده کنید. مثال‌هایی از درخواست‌های Curl در زیر آورده شده است:

- ایجاد یک URL کوتاه:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"original_url": "https://example.com"}' http://localhost:8000/api/shorten/
  ```

- دریافت آمار یک URL کوتاه:

  ```bash
  curl http://localhost:8000/api/stats/<short_url>/
  ```

- تغییر مسیر به URL اصلی:

  ```bash
  curl http://localhost:8000/<short_url>/
  ```
