var express = require('express');
var router = express.Router();

const CaseDetail = require('../../services/case-detail');

router.post("/get-all", (req, res, next) => {
    try {
        let data = req.body

        CaseDetail.getAll({
            case_date: data.case_date,
            state: data.code
        }).then(response => {
            res.json(response);
        });
    } catch (err) {
        console.error("Opps!! Something went wrong:", err.message);
    }
});

router.post("/get-covid-19-case-by-gender", (req, res, next) => {
    try {
        let data = req.body

        CaseDetail.getCovid19CaseByGender(data).then(response => {
            res.json(response);
        });
    } catch (err) {
        console.error("Opps!! Something went wrong:", err.message);
    }
});

router.post("/get-covid-19-case-by-race", (req, res, next) => {
    try {
        let data = req.body

        CaseDetail.getCovid19CaseByRace(data).then(response => {
            res.json(response);
        });
    } catch (err) {
        console.error("Opps!! Something went wrong:", err.message);
    }
});

router.post("/get-covid-19-case-by-age", (req, res, next) => {
    try {
        let data = req.body

        CaseDetail.getCovid19CaseByAge(data).then(response => {
            res.json(response);
        });
    } catch (err) {
        console.error("Opps!! Something went wrong:", err.message);
    }
});

router.post("/get-covid-19-case-by-type", (req, res, next) => {
    try {
        let data = req.body

        CaseDetail.getCovid19CaseByType(data).then(response => {
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
