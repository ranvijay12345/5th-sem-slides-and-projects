const db = require('../../utils/db')

const Dashboard = (() => {

    const getAllRecords = req =>
        new Promise((resolve, reject) => {

            let where = `where id > 0`

            if (req.case_date) {

                where = where + ` and case_date = '${req.case_date}'`
            }

            if (req.code) {

                where = where + ` and state = '${req.code}'`
            }

            let sql = `select * from patient ${where} order by id`

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
    const getAll = req =>
        new Promise((resolve, reject) => {

            let where = `where b.id > 0`

            console.log(req)

            if (req.case_date) {

                where = where + ` and b.case_date = '${req.case_date}'`
            }


            let sql = `select x.code, x.description, (case when y.total_case is null then 0 else y.total_case end) as total_case from states x left join (select a.id, count(a.code) as total_case from states a left join patient b on a.code = b.state ${where} group by b.state order by count(a.code) desc) y on x.id = y.id order by total_case desc;`

            db.query(sql, (err, results) => {
                if (err) {
                    reject({
                        error: true,
                        details: err
                    });
                    return
                }

                /**workaround total */
                let overall_total_case = 0
                let labels = []
                let values = []
                for (let i = 0; i < results.length; i++) {
                    overall_total_case = overall_total_case + results[i].total_case
                    labels.push(results[i].description)
                    values.push(results[i].total_case)
                }

                resolve({ error: false, data: results, overall_total_case, labels, values })

            })
        })

    const getAllStates = req =>
        new Promise((resolve, reject) => {

            let sql = `select * from states order by description`

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

    const getAllCaseDate = req =>
        new Promise((resolve, reject) => {

            let sql = `select case_date as code, DATE_FORMAT(case_date,'%d-%b-%Y') as description from patient group by case_date`

            console.log(sql)
            db.query(sql, (err, results) => {
                console.log(err)
                console.log(results)
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
        getAllStates,
        getAllCaseDate,
        getPercentageByGender,
        getCovidCaseByState,
        insertSampleData,
        getAllRecords
    }
})()

module.exports = Dashboard
