DROP TABLE IF EXISTS gold_dim_channel;   
CREATE TABLE IF NOT EXISTS gold_dim_channel (
    channel_sk      CHAR(26)     NOT NULL,
    channel_name    VARCHAR(100) NOT NULL,
    dw_created_at   DATETIME     NOT NULL,

    PRIMARY KEY (channel_sk),
    UNIQUE KEY uk_channel_name (channel_name)
) ENGINE=InnoDB;
