require(RMixpanel)
require(lubridate)

datasets  <- list()
datasets  <- c(datasets, list(
  # c("HKG - Cordis, Hong Kong", 9, 2016),
  # c("HKG - Cordis, Hong Kong", 10, 2016),
  # c("HKG - Cordis, Hong Kong", 11, 2016),
  # c("HKG - Cordis, Hong Kong", 12, 2016),
  # c("HKG - Cordis, Hong Kong", 1, 2017),
  # c("HKG - Cordis, Hong Kong", 2, 2017),
  # c("HKG - Dorsett Tsuen Wan Hong Kong", 9, 2016),
  # c("HKG - Dorsett Tsuen Wan Hong Kong", 10, 2016),
  # c("HKG - Dorsett Tsuen Wan Hong Kong", 11, 2016),
  # c("HKG - Dorsett Tsuen Wan Hong Kong", 12, 2016),
  # c("HKG - Dorsett Tsuen Wan Hong Kong", 1, 2017),
  # c("HKG - Dorsett Tsuen Wan Hong Kong", 2, 2017),
  c("UAE - Dubai - Dusit Thani Dubai", 1, 2017),
  # c("UAE - Dubai - Dusit Thani Dubai", 2, 2017),
  c("UAE - Dubai - Fairmont The Palm", 1, 2017),
  c("UAE - Dubai - Fairmont The Palm", 2, 2017),
  c("UAE - Dubai - Le Meridien Mina Seyahi Beach Resort & Marina", 1, 2017),
  c("UAE - Dubai - Le Meridien Mina Seyahi Beach Resort & Marina", 2, 2017),
  c("UAE - Dubai - The Westin Dubai Mina Seyahi", 1, 2017),
  c("UAE - Dubai - The Westin Dubai Mina Seyahi", 2, 2017)
))

account = mixpanelCreateAccount(
  "Launcher 6.031 HK",
  token="6c29862add298fba05d9fd796a51e441",
  key="79e6e24e3eb5328f09a63c722a91250e",
  secret="5e6cdddbceb52e9eb064bbf05f8d8510"
)

first_day <- function(month, year) {
  return(ymd(paste0(year, "-", month, "-01")))
}

last_day <- function(month, year) {
  last <- first_day(month, year)
  day(last) <- days_in_month(last)
  return(last)
}

get_csv <- function(dataset) {
  for(i in dataset) {
    counter   <- i[1]
    month     <- i[2]
    year      <- i[3]

    events <- mixpanelGetEvents(
      account,
      "Screen View", # event
      first_day(month, year), # from
      last_day(month, year), # to
      daysPerBlock = 10,
      select = TRUE, # select = [ARRAY PROPERTIES]
      where = paste0("(properties[\"Service Counter\"] == \"", counter, "\")"),
      verbose = TRUE
    )

    write.csv(events, paste0("~/r/mixpanel/", counter, "_", first_day(month, year), ".csv"))

  }
}


setwd("~/r/temp")
get_csv(datasets)










# c("time","distinct_id","Longitude","Latitude","Have Hotel Home","Hotel Guest Id","Is Home"]
