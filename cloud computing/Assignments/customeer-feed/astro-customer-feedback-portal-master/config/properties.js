const PROPS = {
    PROD: true,
    DB_LOCAL: {
        // HOST: '127.0.0.1',
        // USERNAME: 'root',
        // PASSWORD: '',
        // SCHEMA: 'astro_feedback_portal',
        // PORT: 3308
        HOST: 'qf5dic2wzyjf1x5x.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
        USERNAME: 'y0hwmohf6y0h6m5o',
        PASSWORD: 'p0fixyjqrj2i26oo',
        SCHEMA: 'jyuc1xar0bxa5yua',
        PORT: 3306
    },
    DB_PROD: {
        HOST: 'qf5dic2wzyjf1x5x.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
        USERNAME: 'y0hwmohf6y0h6m5o',
        PASSWORD: 'p0fixyjqrj2i26oo',
        SCHEMA: 'jyuc1xar0bxa5yua',
        PORT: 3306
    }
}

module.exports = PROPS