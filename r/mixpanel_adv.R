require(RMixpanel)
require(lubridate)

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

get_csv_hk <- function(day) {
    events <- mixpanelGetEvents(
      account,
      "Advertising Banner View", # event
      # first_day(month, year), # from
      # last_day(month, year), # to
      day,
      day,
      daysPerBlock = 10,
      select = TRUE, # select = [ARRAY PROPERTIES]
      where = "(\"Feed\" in properties[\"Screen Name\"]) and (defined (properties[\"Screen Name\"]))",
      verbose = TRUE
    )
    write.csv(events, paste0("~/r/adv/adv_", day, ".csv"))
}

setwd("~/r/temp")
get_csv_hk("2017-06-17")
get_csv_hk("2017-06-18")
get_csv_hk("2017-06-19")
get_csv_hk("2017-06-20")
get_csv_hk("2017-06-21")
get_csv_hk("2017-06-22")
get_csv_hk("2017-06-23")
get_csv_hk("2017-06-24")
get_csv_hk("2017-06-25")
get_csv_hk("2017-06-26")
get_csv_hk("2017-06-27")
get_csv_hk("2017-06-28")
get_csv_hk("2017-06-29")
get_csv_hk("2017-06-30")










# c("time","distinct_id","Longitude","Latitude","Have Hotel Home","Hotel Guest Id","Is Home"]
