# Network data #

#Reading in data
library(tidyverse)
library(xlsx)
library(igraph)


# Reading in the network data
# Site 10
network10402 <- read.xlsx("/Users/Andrew/Library/CloudStorage/Box-Box/CLAVES/2021_2022_Data/Pretesting/Raw Data/Network Survey - Yonkers - Class 10402_December 8, 2021_12.16.xlsx",
                       sheetName = "Sheet0",
                       password = "claves2021")

network10504 <- read.xlsx("/Users/Andrew/Library/CloudStorage/Box-Box/CLAVES/2021_2022_Data/Pretesting/Raw Data/Network Survey - Yonkers - Class 10504_December 8, 2021_12.20.xlsx",
                          sheetName = "Sheet0",
                          password = "claves2021")

# Site 20
network20203 <- read.xlsx("/Users/Andrew/Library/CloudStorage/Box-Box/CLAVES/2021_2022_Data/Pretesting/Raw Data/Network Survey - Yonkers - Class 20203_December 8, 2021_12.24.xlsx",
                          sheetName = "Sheet0",
                          password = "claves2021")

network20205 <- read.xlsx("/Users/Andrew/Library/CloudStorage/Box-Box/CLAVES/2021_2022_Data/Pretesting/Raw Data/Network Survey - Yonkers - Class 20205_December 8, 2021_12.25.xlsx",
                          sheetName = "Sheet0",
                          password = "claves2021")

# Creating list of consent files to create consent list from
consent_names <- list("/Users/Andrew/Library/CloudStorage/Box-Box/CLAVES/2021_2022_Data/Consents/Fermi - Joyce (Sean review)/FermiConsentedStudentsList.xlsx",
                      "/Users/Andrew/Library/CloudStorage/Box-Box/CLAVES/2021_2022_Data/Consents/Hostos - Catherine (Summer review)/HostosConsentedStudentsList.xlsx",
                      "/Users/Andrew/Library/CloudStorage/Box-Box/CLAVES/2021_2022_Data/Consents/Hostos - Catherine (Summer review)/HostosConsentedStudentsList_OCT_ADDITION.xlsx",
                      "/Users/Andrew/Library/CloudStorage/Box-Box/CLAVES/2021_2022_Data/Consents/Scholastic - Summer (Catherine review)/ScholasticConsentedStudents (Small Version).xlsx")

# Creating consent df
consent <- map_dfr(consent_names, 
                   read.xlsx,
                   sheetName = "Consented Students",
                   password = "claves2021")


claves_el <- function(network, consent, class_number, class_size) {
  consent <- consent %>% filter(Class == class_number)
  d1 <- merge(network, consent, 
              by.x = "Capti_ID", 
              by.y = "Capti.ID",
              all.x = T,
              all.y = F) %>% 
    arrange(desc(Progress))
  # Subset just the columns with the language questions for each student 
  d2 = d1[,names(d1)[grepl('(.*)(x\\d+)(.*)', names(d1), ignore.case = F)]]
  # Drop columns with work
  d2 <- d2 %>% select(!contains("Work"))
  # Add name column with first and last name
  d2$name = d1$First.Name
  # Moves name variable to the beginning of the df 
  d2 = d2 %>% relocate(name)
  # Eliminates second row variable names 
  d3 = d2[2:nrow(d2),]
  # Renames columns with names from old second row
  names(d3) = d2[1,] %>% as.list %>% unlist
  # Add name to name column
  colnames(d3)[1] <- "stud_name"
  # Pivots data to edgelist form 
  d4 = tidyr::pivot_longer(d3, cols = names(d3)[2:ncol(d3)])
  # Identifies valid data where language option was selected (but missing if student selected but language question unanswered)
  d5 = d4 %>% unique %>% arrange(name) %>% filter(value != "")
  # Renames variables to more intuitive
  names(d5) = c('Student Selecting', 'Student Selected', 'Student-Student Language Choice')
  # Drops extra text from name of selected student 
  d5$`Student Selected` = stringr::str_replace_all(d5$`Student Selected`, fixed(' - Please tell us what language you use when you talk with [Field-1].'), '')
  # Create extra df to solve missing language but selected student issue above
  d6 = d1
  # Add name variable to merge on
  d6$name = d1$First.Name
  # Create simple edgelist 
  d6 <- d6 %>% 
    select(name,
           Hang_Out_Roster) %>% 
    separate_rows(Hang_Out_Roster,
                  sep = ",") %>% 
    filter(!is.na(Hang_Out_Roster))
  # Eliminate extra variable name
  d6 = d6[2:nrow(d6),]
  # Merges back to correct for issue with selected name but no selected language 
  d7 <- merge(d5, d6, by.x = c("Student Selecting", "Student Selected"), by.y = c("name", "Hang_Out_Roster"), all = T)
  # Creates graph and eliminates multiple edges (where both kids picked each other) and loops where kids picked themselves
  d7 <- d7 %>% 
    graph_from_data_frame(directed = F) %>% 
    simplify(remove.multiple = T, remove.loops = T)
  # Runs degree of graph
  test <- degree(d7)
  # Turns degree output into tibble
  test <- tibble(First.Name = names(test), 
                 degree = test,
                 degree_norm = test/(class_size - 1))
  # Merges back with original dataset
  test2 <- merge(consent, test)
  return(test2)
}

test3 <- claves_el(network10402, consent, 402, 22)





# Test code for function

consent10402 <- consent %>% filter(Class == 402)
d1 <- merge(network10402, consent10402, 
            by.x = "Capti_ID", 
            by.y = "Capti.ID",
            all.x = T,
            all.y = F) %>% 
  arrange(desc(Progress))
# Subset just the columns with the language questions for each student 
d2 = d1[,names(d1)[grepl('(.*)(x\\d+)(.*)', names(d1), ignore.case = F)]]
# Drop columns with work
d2 <- d2 %>% select(!contains("Work"))
# Add name column with first and last name
d2$name = d1$First.Name
# Moves name variable to the beginning of the df 
d2 = d2 %>% relocate(name)
# Eliminates second row variable names 
d3 = d2[2:nrow(d2),]
# Renames columns with names from old second row
names(d3) = d2[1,] %>% as.list %>% unlist
# Add name to name column
colnames(d3)[1] <- "stud_name"
# Pivots data to edgelist form 
d4 = tidyr::pivot_longer(d3, cols = names(d3)[2:ncol(d3)])
# Identifies valid data where language option was selected (but missing if student selected but language question unanswered)
d5 = d4 %>% unique %>% arrange(name) %>% filter(value != "")
# Renames variables to more intuitive
names(d5) = c('Student Selecting', 'Student Selected', 'Student-Student Language Choice')
# Drops extra text from name of selected student 
d5$`Student Selected` = stringr::str_replace_all(d5$`Student Selected`, fixed(' - Please tell us what language you use when you talk with [Field-1].'), '')
# Create extra df to solve missing language but selected student issue above
d6 = d1
# Add name variable to merge on
d6$name = d1$First.Name
# Create simple edgelist 
d6 <- d6 %>% 
  select(name,
         Hang_Out_Roster) %>% 
  separate_rows(Hang_Out_Roster,
                sep = ",") %>% 
  filter(!is.na(Hang_Out_Roster))
# Eliminate extra variable name
d6 = d6[2:nrow(d6),]
# Merges back to correct for issue with selected name but no selected language 
d7 <- merge(d5, d6, by.x = c("Student Selecting", "Student Selected"), by.y = c("name", "Hang_Out_Roster"), all = T)
# Creates graph and eliminates multiple edges (where both kids picked each other) and loops where kids picked themselves
d7 <- d7 %>% 
  graph_from_data_frame(directed = F) %>% 
  simplify(remove.multiple = T, remove.loops = T)
# Runs degree of graph
test <- degree(d7)
# Turns degree output into tibble
test <- tibble(First.Name = names(test), 
               degree = test,
               degree_norm = test/(22-1))
# Merges back with original dataset
test2 <- merge(consent10402, test)


consent10504 <- consent %>% filter(Class == 504)
d1 <- merge(network10504, consent10504, 
            by.x = "Capti_ID", 
            by.y = "Capti.ID",
            all.x = T,
            all.y = F) %>% 
  arrange(desc(Progress))
# Subset just the columns with the language questions for each student 
d2 = d1[,names(d1)[grepl('(.*)(x\\d+)(.*)', names(d1), ignore.case = F)]]
# Drop columns with work
d2 <- d2 %>% select(!contains("Work"))
# Add name column with first and last name
d2$name = d1$First.Name
# Moves name variable to the beginning of the df 
d2 = d2 %>% relocate(name)
# Eliminates second row variable names 
d3 = d2[2:nrow(d2),]
# Renames columns with names from old second row
names(d3) = d2[1,] %>% as.list %>% unlist
# Add name to name column
colnames(d3)[1] <- "stud_name"
# Pivots data to edgelist form 
d4 = tidyr::pivot_longer(d3, cols = names(d3)[2:ncol(d3)])
# Identifies valid data where language option was selected (but missing if student selected but language question unanswered)
d5 = d4 %>% unique %>% arrange(name) %>% filter(value != "")
# Renames variables to more intuitive
names(d5) = c('Student Selecting', 'Student Selected', 'Student-Student Language Choice')
# Drops extra text from name of selected student 
d5$`Student Selected` = stringr::str_replace_all(d5$`Student Selected`, fixed(' - Please tell us what language you use when you talk with [Field-1].'), '')
# Create extra df to solve missing language but selected student issue above
d6 = d1
# Add name variable to merge on
d6$name = d1$First.Name
# Create simple edgelist 
d6 <- d6 %>% 
  select(name,
         Hang_Out_Roster) %>% 
  separate_rows(Hang_Out_Roster,
                sep = ",") %>% 
  filter(!is.na(Hang_Out_Roster))
# Eliminate extra variable name
d6 = d6[2:nrow(d6),]
# Merges back to correct for issue with selected name but no selected language 
d7 <- merge(d5, d6, by.x = c("Student Selecting", "Student Selected"), by.y = c("name", "Hang_Out_Roster"), all = T)
# Creates graph and eliminates multiple edges (where both kids picked each other) and loops where kids picked themselves
d7 <- d7 %>% 
  graph_from_data_frame(directed = F) %>% 
  simplify(remove.multiple = T, remove.loops = T)
# Runs degree of graph
test <- degree(d7)
# Turns degree output into tibble
test <- tibble(First.Name = names(test), 
               degree = test,
               degree_norm = test/(29-1))
# Merges back with original dataset
test2 <- merge(consent10504, test)
test3 <- merge(test2, consent, all = T)

# Checking messed up emails
d2 <- d1 %>% filter(is.na(First.Name))

# 20203
consent20203 <- consent %>% filter(Class == 203)
d1 <- merge(network20203, consent20203, 
            by.x = "Capti_ID", 
            by.y = "Capti.ID",
            all.x = T,
            all.y = F) %>% 
  arrange(desc(Progress))

d2 <- d1 %>% filter(is.na(First.Name))

#20205
consent20205 <- consent %>% filter(Class == 205)
d1 <- merge(network20205, consent20205, 
            by.x = "Capti_ID", 
            by.y = "Capti.ID",
            all.x = T,
            all.y = F) %>% 
  arrange(desc(Progress))

d2 <- d1 %>% filter(is.na(First.Name))
