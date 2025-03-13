# 🏆 Job Portal API

A **Django REST Framework** based API for job seekers and recruiters. Candidates can search & apply for jobs, while recruiters can post & manage job applications.  

## 🚀 Features
- **User Authentication** (JWT-based)
- **Role-based Access Control** (Candidate & Recruiter)
- **Job Management** (CRUD operations)
- **Job Applications** (Apply, View, Accept/Reject)
- **Profile Management**

---

## 🔐 Authentication Endpoints

| **Method** | **Endpoint**     | **Description** |
|------------|-----------------|-----------------|
| `POST`     | `/api/register/` | Register a new user (Candidate/Recruiter) |
| `POST`     | `/api/login/`    | Login and get JWT tokens |

---

## 💼 Job Management Endpoints

| **Method** | **Endpoint**         | **Description** |
|------------|----------------------|-----------------|
| `GET`      | `/api/jobs/`         | List all jobs |
| `POST`     | `/api/jobs/`         | Create a new job (Recruiter only) |
| `GET`      | `/api/jobs/{id}/`    | Retrieve details of a specific job |
| `PUT`      | `/api/jobs/{id}/`    | Update a job (Recruiter only) |
| `DELETE`   | `/api/jobs/{id}/`    | Delete a job (Recruiter only) |

---

## 📄 Job Application Endpoints

| **Method** | **Endpoint**              | **Description** |
|------------|--------------------------|-----------------|
| `POST`     | `/api/jobs/{id}/apply/`  | Apply for a job (Candidate only) |
| `GET`      | `/api/applications/`     | View all applications (Recruiter only) |
| `GET`      | `/api/applications/{id}/` | Retrieve details of an application (Recruiter only) |
| `PUT`      | `/api/applications/{id}/status/` | Accept/Reject a job application (Recruiter only) |

---

## 🏠 User Profile Endpoints

| **Method** | **Endpoint**          | **Description** |
|------------|----------------------|-----------------|
| `GET`      | `/api/profile/`      | View user profile (Authenticated users) |
| `PUT`      | `/api/profile/update/` | Update user profile |

---

## Login Test

![Login Test](https://github.com/Babupydev/job-portal-api/blob/226fbf130aebe78891011002e68dc94fd14294ec/LOGIN.png)
