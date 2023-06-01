## Exam

---

### About project:

- It is simple application on `Flask` with based `API` 
- Application runs from `Docker` container
- Realize `CI/CD` logic and deploy at server with `GitHub Actions`


---

### How to use:

---

#### You can use `skygpt.site` address and send your requests on this site, or you can do it from your local machine

---

1) Copy this project on your local machine `git clone `
2) Write in a terminal this command `docker-compose up --build -d`
3) Open an application, which can send **GET/POST/PUT/DELETE** methods, f.e `Postman` and write in the browse page this
   address `http://localhost/`
4) Write your request and push "SEND" button
5) Receive a response in `JSON` format from the application

---

### Data for post:

```json
[
  {
    "title": "skypro",
    "date": "2023-06-01"
    "teacher": "Ivan Fufaev",
    "classroom": 403
  },
  {
    "title": "weekly planing",
    "date": "2023-06-03"
    "teacher": "Evgeniy Smirnova",
    "classroom": 408
  },
  {
    "title": "cooking",
    "date": "2023-06-01"
    "teacher": "Siemens",
    "classroom": 333
  }
]
```

## Virtual machine supported by _Yandex Cloud_