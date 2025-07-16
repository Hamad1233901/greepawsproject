# GreenPaws Veterinary Clinic Management System

**Student Name:** Hamad Ahmad  
**Student ID:** 20052177  
**Programme:** MSc in IS & Computing  
**Module Title:** Programming for Information Systems  
**Module Code:** B9IS123  
**Lecturer:** Paul Laird  

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [System Requirements](#system-requirements)  
3. [System Architecture](#system-architecture)  
4. [Features & Functional Highlights](#features--functional-highlights)  
5. [Project Structure](#project-structure)  
6. [Technologies Used](#technologies-used)  
7. [Setup Instructions](#setup-instructions)  
8. [Testing Strategy](#testing-strategy)  
9. [Resources & Attribution](#resources--attribution)  
10. [Project Location](#project-location)  
11. [Final Notes](#final-notes)

---

## Project Overview

**GreenPaws** is a lightweight, full-stack veterinary clinic management system built as a proof-of-concept application for small-scale vet practices. It supports digital record-keeping of clients, their pets, and visit histories, allowing for efficient CRUD operations.

### Business Context

GreenPaws was designed in response to challenges faced by a small but growing veterinary clinic. The traditional paper-based record system led to:

- Lost or incomplete medical records  
- Difficulty tracking vaccinations and treatments  
- Inefficiency in client and appointment handling  

GreenPaws digitizes and streamlines this process using modern web technologies.

---

## System Requirements

The system meets the following academic and functional requirements:

### Functional Requirements

- [x] Create, Read, Update, Delete operations for:
  - Client records
  - Pet profiles
  - Visit records
- [x] Input validation via JavaScript  
- [x] Frontend communication with backend via Fetch API  
- [x] Foreign key enforcement using SQLite for relational integrity  
- [x] Live DOM updates without page reloads  
- [x] Simple, unstyled HTML interface (per module brief)  

---

## System Architecture

GreenPaws follows a **Client-Server architecture** with a decoupled frontend and backend:

### Frontend

- Built using **HTML5**, **CSS3**, and **Vanilla JavaScript**
- Uses `fetch()` to call backend API endpoints
- Dynamically renders data using JavaScript DOM manipulation

### Backend

- Implemented using **Python Flask**
- RESTful API serving JSON data
- Uses **SQLite** with foreign key relationships
- CORS support via `Flask-CORS` for cross-origin access

---

## Features & Functional Highlights

| Feature                       | Description                                                                 | ChatGPT Contribution                        |
|------------------------------|-----------------------------------------------------------------------------|---------------------------------------------|
| **Client Management**         | Add/edit/delete client info (name, contact, CNIC)                          | Designed logic flow and input structure     |
| **Pet Registration**          | Link pet details to client records (type, breed, age)                      | Schema and relational design via ChatGPT    |
| **Visit Logging**             | Store symptoms, diagnosis, treatment, and schedule follow-up visits        | CRUD routes and DB logic drafted using ChatGPT |
| **Dynamic Table Updates**     | Live updates of HTML tables using JavaScript DOM                           | DOM scripting logic generated with ChatGPT  |
| **API Calls (AJAX)**          | Communicate with backend using Fetch API                                   | Explanation and example from ChatGPT        |
| **Input Validation**          | Client-side input validation for forms                                     | Validation logic guided and improved via ChatGPT |
| **SQLite DB Schema**          | Tables and foreign keys to enforce relationships                           | Schema design and constraints from ChatGPT  |
| **CORS Setup**                | Flask-CORS integration to enable frontend-backend interaction              | CORS config written using ChatGPT prompts   |

---

## Project Structure

```plaintext
greepawsproject/
├── backend/
│   └── app.py             # Flask application with routes and DB logic
├── Frontend/
│   ├── index.html         # Web interface
│   ├── style.css          # Minimal styling
│   └── script.js          # JavaScript functionality
├── tests/                 # Placeholder for unit/integration tests
├── README.md              # Project documentation

> Manual testing was conducted during development. 

## Resources & Attribution

All assistance for this project was provided exclusively by **ChatGPT (OpenAI)**.All AI-generated suggestions were manually tested, reviewed, and integrated by the student to meet academic integrity requirements of module **B9IS123**.

### Attribution Breakdown (ChatGPT-Assisted Tasks)

| Area of Work                  | ChatGPT Contribution                                                                 |
|------------------------------|---------------------------------------------------------------------------------------|
| **Relational Database Schema** | Helped define and normalize SQLite tables (Clients, Pets, Visits) using foreign keys |
| **Flask API Routes**         | Guided creation of RESTful routes (`GET`, `POST`, `PUT`, `DELETE`) for all entities   |
| **Form Validation (JS)**     | Assisted in writing client-side validation using regex, empty checks, and logic flow |
| **JavaScript Fetch Logic**   | Provided syntax and structure for `fetch()` API calls to communicate with Flask API  |
| **Dynamic DOM Updates**      | Helped build functions to populate and update HTML tables with live data             |
| **CORS Configuration**       | Suggested correct usage of `flask-cors` to enable frontend-backend communication     |
| **Error Handling**           | Helped design frontend and backend error messages and response handling              |
| **Testing Strategy Outline** | Advised on designing unit and integration test plans for both frontend and backend   |
| **Project Documentation**    | Guided layout, formatting, and explanation of content in this `README.md` file       |
| **Code Debugging**           | Suggested fixes for specific issues encountered during development                   |

---

## Attribution Summary

- This entire project was developed solely by **Hamad Ahmad (ID: 20052177)** for the **MSc in IS & Computing** programme, module **B9IS123 – Programming for Information Systems**.
- No code or support was taken from classmates, online tutorials, Stack Overflow, GitHub repositories, or any third-party source.
- All **external guidance was exclusively provided by ChatGPT**, in compliance with the module’s rules on GenAI tools.
- Each AI-assisted segment was:
  - Prompted and reviewed individually
  - Manually modified, tested, and integrated by the student
  - Logged via Git commits alongside the project code
- No AI-generated code was used "as-is" without verification or customization.
- **Every instance of assistance** was transparently declared here as required by the module’s academic integrity policy.

---

## Final Notes

> This README is designed to reflect both the technical implementation and compliance with academic integrity requirements. All logic was implemented by the student with reference-only support from ChatGPT.

---
