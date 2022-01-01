const db = require('../../utils/db')
const Promise = require('bluebird');

const Review = (() => {
    const getAll = req =>
        new Promise((resolve, reject) => {
            const query = `select a.id, a.review_id, a.user_id, a.title, b.email, c.review_type_id, c.description, c.total_like, c.total_dislike, d.description as review_desc from review a left join user b on a.user_id = b.user_id left join review_detail c on a.review_id = c.review_id left join review_type d on d.id = c.review_type_id order by c.total_like desc`

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

    const addNew = req =>
        new Promise(async (resolve, reject) => {
            let email = req.data.email
            let user_id = new Date().getTime() + Math.floor((Math.random() * 1000) + 1);
            let title = req.data.title
            let review_type = req.data.review_type
            let description = req.data.description
            let query = `insert into user (user_id, email) values ('${user_id}', '${email}');`
            await db.query(query, (err, results) => {
                if (err) {
                    reject({
                        error: true,
                        details: err
                    });
                    return
                }
            })

            let review_id = new Date().getTime() + Math.floor((Math.random() * 1000) + 1);
            query = `insert into review (review_id, user_id, title) values ('${review_id}','${user_id}', '${title}');`
            await db.query(query, (err, results) => {
                if (err) {
                    reject({
                        error: true,
                        details: err
                    });
                    return
                }
            })

            query = `insert into review_detail (review_id, review_type_id, description) values (${review_id}, ${review_type}, '${description}');`
            await db.query(query, (err, results) => {
                if (err) {
                    reject({
                        error: true,
                        details: err
                    });
                    return
                }
            })

            resolve({ error: false })

        })

    const updateRating = req =>
        new Promise((resolve, reject) => {
            let total_like = req.data.total_like
            let total_dislike = req.data.total_dislike
            let review_id = req.data.id
            const query = `update review_detail set total_like = ${total_like}, total_dislike = ${total_dislike} where review_id = ${review_id}`

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

    const getReviewTypes = req =>
        new Promise((resolve, reject) => {
            const query = `select id, description from review_type`

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

    const getReviewByEmail = email =>
        new Promise((resolve, reject) => {
            const query = `select a.id, a.review_id, a.user_id, a.title, b.email, c.review_type_id, c.description, c.total_like, c.total_dislike, d.description as review_desc from review a left join user b on a.user_id = b.user_id left join review_detail c on a.review_id = c.review_id left join review_type d on d.id = c.review_type_id where b.email= "${email}" order by c.total_like desc`

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
        getAll,
        addNew,
        updateRating,
        getReviewTypes,
        getReviewByEmail
    }
})()

module.exports = Review
