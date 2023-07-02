# CMS Application API

This is a CMS (Content Management System) application API that allows you to manage users, posts/blogs, and likes. It provides CRUD (Create, Read, Update, Delete) operations for each table and follows certain access rules.

## Tables

1. User
   - Fields: user ID, name, email, password, and other relevant details.

2. Post/Blog
   - Fields: post ID, title, description, content, creation date, and other relevant details.

3. Like
   - Fields: like ID, post ID, user ID, and other relevant details.

## API Endpoints

### User Endpoints

- `POST /users/`: Create a new user.
- `GET /users/{id}/`: Retrieve a specific user.
- `PUT /users/{id}/`: Update the details of a specific user.
- `DELETE /users/{id}/`: Delete a specific user.

### Post/Blog Endpoints

- `POST /posts/`: Create a new post/blog.
- `GET /posts/{id}/`: Retrieve a specific post/blog.
- `PUT /posts/{id}/`: Update the details of a specific post/blog.
- `DELETE /posts/{id}/`: Delete a specific post/blog.

### Like Endpoints

- `POST /likes/`: Create a new like for a post/blog.
- `GET /likes/{id}/`: Retrieve a specific like.
- `PUT /likes/{id}/`: Update the details of a specific like.
- `DELETE /likes/{id}/`: Delete a specific like.


### Access Rules

- Access to the PUT/DELETE APIs for the Post/Blog table is restricted to the owner of the post/blog.
- Any user can access the GET API for a post/blog if it is public. For private posts/blogs, only the owner should be able to access them.
- There is only one API endpoint for any given query. Retrieval of both the post/blog and its likes is completed within a single query.

