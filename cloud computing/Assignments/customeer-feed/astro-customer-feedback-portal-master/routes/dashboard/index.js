var express = require('express');
var router = express.Router();

const Dashboard = require('../../services/dashboard');

router.post("/get-all-records", (req, res, next) => {
    try {
        let data = req.body

        Dashboard.getAllRecords(data).then(response => {
            res.json(response);
        });
    } catch (err) {
        console.error("Opps!! Something went wrong:", err.message);
    }
});

router.post("/get-all", (req, res, next) => {
    try {
        let data = req.body

        Dashboard.getAll({
            case_date: data.case_date,
            state: data.state
        }).then(response => {
            res.json(response);
        });
    } catch (err) {
        console.error("Opps!! Something went wrong:", err.message);
    }
});

router.get("/get-all-states", (req, res, next) => {
    try {
        let data = req.body

        Dashboard.getAllStates().then(response => {
            res.json(response);
        });
    } catch (err) {
        console.error("Opps!! Something went wrong:", err.message);
    }
});

router.get("/get-all-case-date", (req, res, next) => {
    try {
        let data = req.body

        Dashboard.getAllCaseDate().then(response => {
            res.json(response);
        });
    } catch (err) {
        console.error("Opps!! Something went wrong:", err.message);
    }
});

router.post("/get-percentage-by-gender", (req, res, next) => {
    try {
        let data = req.body

        Dashboard.getPercentageByGender({
            case_date: data.case_date,
            state: data.state
        }).then(response => {
            res.json(response);
        });
    } catch (err) {
        console.error("Opps!! Something went wrong:", err.message);
    }
});

router.post("/get-covid-case-by-state", (req, res, next) => {
    try {
        let data = req.body

        Dashboard.getCovidCaseByState({
            state: data.state
        }).then(response => {
            res.json(response);
        });
    } catch (err) {
        console.error("Opps!! Something went wrong:", err.message);
    }
});

router.post("/insert-sample-data", (req, res, next) => {
    try {
        
        let data = req.body
        Dashboard.insertSampleData(data).then(response => {
            res.json(response);
        });
    } catch (err) {
        console.error("Opps!! Something went wrong:", err.message);
    }
});


module.exports = router;
