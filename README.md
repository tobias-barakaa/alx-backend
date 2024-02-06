# Node.js Backend with SQL (PostgreSQL) Configuration Guide

This guide provides instructions for configuring a Node.js backend application with SQL (PostgreSQL) database. You'll learn how to set up the database, configure the Node.js environment, and establish connections between the backend and the database.

## Prerequisites

Before starting, ensure you have the following installed:

- Node.js (latest LTS version recommended)
- PostgreSQL database server
- npm (Node.js package manager)

## Setting Up PostgreSQL Database

1. **Install PostgreSQL**: Download and install PostgreSQL from the official website or package manager of your operating system.

2. **Start PostgreSQL Service**: Start the PostgreSQL service on your local machine. The commands may vary depending on your operating system.

3. **Create Database**: Create a new database for your Node.js application using the PostgreSQL command-line interface or a GUI tool like pgAdmin.

    ```bash
    createdb mydatabase
    ```

4. **Create Tables**: Design and create the necessary tables within your PostgreSQL database to store application data.

## Configuring Node.js Backend

1. **Initialize Node.js Project**: Create a new Node.js project or navigate to an existing one.

    ```bash
    mkdir my-backend-app
    cd my-backend-app
    npm init -y
    ```

2. **Install Dependencies**: Install necessary Node.js packages such as `express`, `pg` (PostgreSQL client for Node.js), and any other dependencies your project requires.

    ```bash
    npm install express pg
    ```

3. **Set Environment Variables**: Store sensitive configuration parameters (e.g., database connection credentials) in environment variables. Create a `.env` file at the root of your project and define these variables.

    ```
    DB_HOST=localhost
    DB_USER=myusername
    DB_PASSWORD=mypassword
    DB_NAME=mydatabase
    ```

4. **Configure Database Connection**: Establish a connection to the PostgreSQL database from your Node.js application. Use the `pg` package to create a connection pool and handle database queries.

    ```javascript
    const { Pool } = require('pg');
    require('dotenv').config();

    const pool = new Pool({
        host: process.env.DB_HOST,
        user: process.env.DB_USER,
        password: process.env.DB_PASSWORD,
        database: process.env.DB_NAME,
        port: 5432 // Default PostgreSQL port
    });

    // Test connection
    pool.query('SELECT NOW()', (err, res) => {
        if (err) {
            console.error('Error connecting to database:', err);
        } else {
            console.log('Connected to database at:', res.rows[0].now);
        }
    });
    ```

5. **Start the Backend Server**: Implement your backend logic using Node.js and Express framework. Start the server to listen for incoming requests.

    ```javascript
    const express = require('express');
    const app = express();
    const PORT = process.env.PORT || 3000;

    // Define routes and middleware

    app.listen(PORT, () => {
        console.log(`Server is running on port ${PORT}`);
    });
    ```

## Running the Backend

To run your Node.js backend application:

1. Ensure PostgreSQL service is running.
2. Start your Node.js application using the command:

    ```bash
    node app.js
    ```

Your backend application should now be up and running, ready to serve requests and interact with the PostgreSQL database.

## Conclusion

Configuring a Node.js backend with a PostgreSQL database allows you to build powerful web applications with robust data storage and retrieval capabilities. By following this guide, you can set up and configure your backend environment efficiently, paving the way for developing feature-rich applications.

