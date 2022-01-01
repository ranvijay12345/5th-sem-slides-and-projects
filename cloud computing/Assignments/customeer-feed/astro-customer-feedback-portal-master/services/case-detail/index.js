const db = require('../../utils/db')

const CaseDetail = (() => {
    const getAll = req =>
        new Promise((resolve, reject) => {

            let where = `where id > 0`

            console.log(req)

            if (req.case_date) {

                where = where + ` and case_date = '${req.case_date}'`
            }

            if (req.state) {

                where = where + ` and state = '${req.state}'`
            }


            let sql = `select * from patient ${where} order by name;`

            db.query(sql, (err, results) => {
                if (err) {
                    reject({
                        error: true,
                        details: err
                    });
                    return
                }

                resolve({ error: false, data: results })

            })
        })

    const getCovid19CaseByGender = req =>
        new Promise((resolve, reject) => {

            let sql = `select count(*) as total_case, a.gender, b.description from patient a left join gender b on a.gender = b.code where a.case_date='${req.case_date}' and a.state='${req.code}' group by a.gender, b.description;`

            db.query(sql, (err, results) => {
                if (err) {
                    reject({
                        error: true,
                        details: err
                    });
                    return
                }

                let labels = []
                let values = []
                let records = []

                console.log(results)

                for (let i = 0; i < results.length; i++) {
                    labels.push(`${results[i].description}(${results[i].total_case})`)
                    values.push(results[i].total_case)
                }

                resolve({ error: false, labels, values })

            })
        })

    const getCovid19CaseByRace = req =>
        new Promise((resolve, reject) => {

            let sql = `select count(*) as total_case, a.race, b.description from patient a left join race b on a.race = b.code where a.case_date='${req.case_date}' and a.state='${req.code}' group by a.race, b.description;`

            db.query(sql, (err, results) => {
                if (err) {
                    reject({
                        error: true,
                        details: err
                    });
                    return
                }

                let labels = []
                let values = []
                let records = []

                for (let i = 0; i < results.length; i++) {
                    labels.push(`${results[i].description}(${results[i].total_case})`)
                    values.push(results[i].total_case)
                }

                resolve({ error: false, labels, values })

            })
        })

    const getCovid19CaseByAge = req =>
        new Promise((resolve, reject) => {

            let sql = `SELECT CASE
                WHEN age BETWEEN 0 and 9 THEN '0-9'
                WHEN age BETWEEN 10 and 19 THEN '10-19'
                WHEN age BETWEEN 20 and 29 THEN '20-29'
                WHEN age BETWEEN 30 and 39 THEN '30-39'
                WHEN age BETWEEN 40 and 49 THEN '40-49'
                WHEN age BETWEEN 50 and 59 THEN '50-59'
                WHEN age BETWEEN 60 and 69 THEN '60-69'
                WHEN age BETWEEN 70 and 79 THEN '70-79'
                WHEN age >= 80 THEN 'Over 80'
                WHEN age IS NULL THEN 'Not Filled In (NULL)' END as description,
            COUNT(*) AS total_case FROM patient where case_date='${req.case_date}' and state='${req.code}' GROUP BY description ORDER BY description`

            db.query(sql, (err, results) => {
                if (err) {
                    reject({
                        error: true,
                        details: err
                    });
                    return
                }

                let labels = []
                let values = []
                let records = []

                for (let i = 0; i < results.length; i++) {
                    labels.push(`${results[i].description}(${results[i].total_case})`)
                    values.push(results[i].total_case)
                }

                resolve({ error: false, labels, values })

            })
        })

    const getCovid19CaseByType = req =>
        new Promise((resolve, reject) => {

            let sql = `select a.code, a.description, count(a.code) as total_case 
            from case_type a 
            left join patient b on a.code = b.case_status 
            where b.case_date='${req.case_date}' and b.state='${req.code}'
            group by b.case_status order by count(a.code) desc;`

            db.query(sql, (err, results) => {
                if (err) {
                    reject({
                        error: true,
                        details: err
                    });
                    return
                }

                let labels = []
                let values = []
                let records = []

                for (let i = 0; i < results.length; i++) {
                    labels.push(`${results[i].description}(${results[i].total_case})`)
                    values.push(results[i].total_case)
                }

                resolve({ error: false, labels, values, results })

            })
        })

    const getAllCaseDate = req =>
        new Promise((resolve, reject) => {

            let sql = `select a.code, a.description, count(a.code) as total_case 
            from case_type a 
            left join patient b on a.code = b.case_status 
            where b.case_date = '2020-03-14' and b.state = '${req.s}'
            group by b.case_status order by count(a.code) desc;`

            db.query(sql, (err, results) => {
                if (err) {
                    reject({
                        error: true,
                        details: err
                    });
                    return
                }

                resolve({ error: false, data: results })

            })
        })

    const getPercentageByGender = req =>
        new Promise((resolve, reject) => {

            let where = `where id > 0`

            if (req.case_date) {

                where = where + ` and report_date = '${req.case_date}'`
            }

            if (req.state) {
                where = where + ` and state = '${req.state}'`
            }

            let sql = `select count(*) as total_male from patient ${where} and gender='Male'`

            let obj = { error: false }

            db.query(sql, (err, results) => {
                if (err) {
                    reject({
                        error: true,
                        details: err
                    });
                    return
                }

                obj.total_male = results

                sql = `select count(*) as total_female from patient ${where} and gender='Female'`

                db.query(sql, (err, results2) => {
                    if (err) {
                        reject({
                            error: true,
                            details: err
                        });
                        return
                    }

                    obj.total_female = results2

                    resolve(obj)

                })

            })
        })

    const getCovidCaseByState = req =>
        new Promise((resolve, reject) => {

            let where = `where a.id > 0`

            if (req.state) {
                where = where + ` and a.state = '${req.state}'`
            }

            let sql = `select a.*, b.*, DATE_FORMAT(a.case_date,'%d-%b-%Y') as case_date_desc from temp_covid_data a left join states b on a.state = b.code ${where} order by case_date asc`

            console.log(sql)

            db.query(sql, (err, results) => {
                if (err) {
                    reject({
                        error: true,
                        details: err
                    });
                    return
                }

                let x_a = []
                let y_a = []

                for (let i = 0; i < results.length; i++) {
                    x_a.push(results[i].case_date_desc)
                    y_a.push(results[i].no_of_case)
                }


                resolve({
                    error: false,
                    data: results,
                    x_a,
                    y_a
                })

            })
        })

    const insertSampleData = req =>
        new Promise((resolve, reject) => {

            try {
                let sql = req.sql

                console.log(sql)

                db.query(sql, [req.values], (err, results) => {
                    if (err) {
                        console.log(err)
                        reject({
                            error: true,
                            details: err
                        });
                        return
                    }

                    resolve({ error: false })

                })
            } catch (error) {
                console.log('ror')
            }

        })


    return {
        getAll,
        getCovid19CaseByGender,
        getCovid19CaseByRace,
        getCovid19CaseByAge,
        getCovid19CaseByType,
        insertSampleData
    }
})()

module.exports = CaseDetail
