const db = require('../../utils/db')

const User = (() => {
    const getAll = req =>
        new Promise((resolve, reject) => {
            const query = `select * from user`

            db.query(query, (err, results) => {
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


    return {
        getAll
    }
})()

module.exports = User
