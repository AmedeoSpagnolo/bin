options(encoding = "UTF-8")      ## for chines
## use getOption("encoding") to see if things were changed

loc <- function(os, language = "english") {
  switch(language,
         english = ifelse(os == "Windows", "English_United States.1252", "en_US.UTF-8"),
         chinese = ifelse(os == "Windows", "Chinese", "zh_CN.utf-8"))
}
## set locale
Sys.setlocale(category = "LC_ALL", loc(Sys.info()[["sysname"]], "chinese"))

print("æ©å ´å¿«ç·è»ç¥¨")
