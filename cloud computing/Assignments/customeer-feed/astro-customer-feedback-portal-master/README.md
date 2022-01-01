# astro-customer-feedback-portal

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 9.1.7.
- Front-End is Angular v9
- Back-End is Node.js(Express framework)
- [Demo](https://astro-customer-feedback-portal.herokuapp.com/)
- Database MySQL

## How to run application from your local

- Open file explorer and open windows command prompt(cmd)
- Paste the following command line and hit `enter`

```bash
git clone https://github.com/kamilmatnoor/astro-customer-feedback-portal.git
```
- Paste the following command line and hit `enter`

```bash
cd astro-customer-feedback-portal
```

- __(**backend)__ next, paste the following command line and hit `enter` 

```bash
npm install
```

```bash
npm start
```

- __(**frontend)__, next, open new command prompt into current directory and paste the following command line and hit `enter` 

```bash
cd angular
```

```bash
npm install
```

- Next, paste the following command line and hit `enter`

```bash
npm start
```

- Open your browser, and access this URL `http://localhost:4200/`

- This application is now running locally, but pointing to `production` database

- In order to change database into `local`, open `config/properties.js` and edit to this following:

```bash
    PROD: false,
    DB_LOCAL: {
        HOST: '127.0.0.1',
        USERNAME: 'root',
        PASSWORD: '',
        SCHEMA: 'astro_feedback_portal',
        PORT: 3306
    }

``` 

- Note: please set `USERNAME`, `PASSWORD`, `PORT` based on your local `mysql`'s credentials(if you are not sure about your local `mysql`'s credentials, you may use current given credentials
- Copy the `mysql` query from `astro_feedback_portal.sql` and run into you local `mysql`
- Rerun command line at __**backend__


Note: any concern or help kindly reach _kamilmatnoor@gmail.com_
