library(tidyverse)
library(treemapify)
library(here)

okcupid_data = read_csv(here("Data", "compressed_okcupid.csv"))


is_categorical = function(x) {
  is.factor(x) | is.logical(x)
}

cat_vars = okcupid_data %>% 
  select(-essay0, -essay9, -education, -body_type, -ethnicity) %>% 
  select_if((function(x) !is.numeric(x))) %>% 
  mutate_all(factor) %>% 
  pivot_longer(dplyr::everything()) %>% 
  table() %>% 
  as_tibble() %>% 
  ggplot(aes(area = n, fill = value, label = value)) + 
  geom_treemap() + 
  geom_treemap_text(color = "white", place = "centre", grow = TRUE) + 
  facet_wrap(~ name) + theme(legend.position = "none") + 
  labs(title = "Categorical Variable Distributions")
ggsave(here("Final Presentation", "cat_vars.png"), plot = cat_vars, height = 6, width = 8, dpi = 400)

okcupid_data %>% select(-X1, -age, -height, -essay0, -essay9, -education) %>% pivot_longer(-c(flesch, long_words)) %>% ggplot(aes(x = log(flesch), y = long_words, color = value)) + geom_point(alpha = 0.3, size = 1) + facet_wrap(~ name) + theme(legend.position = "none") + labs(title = "Flesch score vs. Long words by Variable")
# needs separate color scheme for each variable

ggsave(here("Final Presentation", "text_vars.png"), height = 6, width = 8, dpi = 400)
