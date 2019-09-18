## Story
* greet
  - utter_greet
* paper_search
  - utter_what_type
* paper_category{"paper_type":"embedded systems"}
    - slot{"paper_type":"embedded systems"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Frank Hutter"}
    - action_ask_for_link
* affirm
  - action_show_link
  - action_ask_for_authors
* affirm
  - action_show_authors
* goodbye
  - utter_goodbye

## Story
* greet
  - utter_greet
* paper_search{"paper_type":"python"}
    - slot{"paper_type":"python"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Frank Hutter"}
    - action_ask_for_link
* affirm+send_authors
  - action_show_link
  - action_show_authors
* goodbye
  - utter_goodbye

## Story
* greet
  - utter_greet
* paper_search{"paper_type":"recommender systems"}
    - slot{"paper_type":"recommender systems"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Frank Hutter"}
    - action_ask_for_link
* deny
  - utter_deny
  - action_ask_for_authors
* affirm
  - action_show_authors
  
## Story
* greet
  - utter_greet
* paper_search{"paper_type":"statistics"}
    - slot{"paper_type":"statistics"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Friedman"}
    - action_ask_for_link
* affirm
  - action_show_link
  - action_ask_for_authors
* deny
  - utter_deny
* goodbye
  -utter_goodbye
  
## Story
* greet
  - utter_greet
* paper_search{"paper_type":"mathematics"}
    - slot{"paper_type":"mathematics"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Frank Hutter"}
* send_authors
  - action_show_authors
* send_link
  - action_show_link
* goodbye
  -utter_goodbye
  
## Story
* greet
  - utter_greet
* paper_search
  - utter_what_type
* paper_category{"paper_type":"learning"}
    - slot{"paper_type":"learning"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Frank Hutter"}
    - action_ask_for_authors
* affirm
  - action_show_authors
* send_link
  - action_show_link
* goodbye
  -utter_goodbye 
  
## Story
* greet
  - utter_greet
* paper_search
  - utter_what_type
* paper_category{"paper_type":"chatbots"}
    - slot{"paper_type":"chatbots"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Frank Hutter"}
    - action_ask_for_link
* affirm+send_authors
  - action_show_link
  - action_show_authors
* goodbye
  -utter_goodbye 
   
## Story
* greet
  - utter_greet
* paper_search
  - utter_what_type
* paper_category{"paper_type":"data minning"}
    - slot{"paper_type":"data minning"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Frank Hutter"}
* send_authors+send_link
  - action_show_link
  - action_show_authors
* goodbye
  -utter_goodbye   

## Story
* greet
  - utter_greet
* paper_search{"paper_type":"physics"}
    - slot{"paper_type":"physics"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Frank Hutter"}
    - action_ask_for_link
* affirm
  - action_show_link
  - action_ask_for_authors
* deny
  - utter_deny
* goodbye
  -utter_goodbye 

## Story
* greet
  - utter_greet
* paper_search{"paper_type":"astrophysics"}
    - slot{"paper_type":"astrophysics"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Frank Hutter"}
    - action_ask_for_link
* deny
  - utter_deny

# Story
* greet
    - utter_greet
* paper_search{"paper_type":"big data"}
    - slot{"paper_type":"big data"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Frank Hutter"}
    - action_ask_for_link
* affirm
    - action_show_link
    - action_ask_for_authors
* affirm
    - action_show_authors
* paper_search{"paper_type":"blockchain development"}
    - slot{"paper_type":"blockchain development"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Frank Hutter"}
    - action_ask_for_authors
* affirm
    - action_show_authors
    - action_ask_for_link
* deny
    - utter_deny
* goodbye
    - utter_goodbye

## Story
* greet
    - utter_greet
* paper_search{"paper_type":"javascript"}
    - slot{"paper_type":"javascript"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/journals/infsof/VazquezBVPM19"}
    - slot{"paper_authors":"Hernán Ceferino Vázquez"}
    - action_ask_for_link
* affirm
    - action_show_link
* send_authors
    - action_show_authors
* paper_search{"paper_type":"artificial intelligence"}
    - slot{"paper_type":"artificial intelligence"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/journals/ker/Parsons94c"}
    - slot{"paper_authors":"S"}
* send_authors
    - action_show_authors
    - action_ask_for_link
* deny
    - utter_deny

## Story
* paper_search{"paper_type":"thermodynamics"}
    - slot{"paper_type":"thermodynamics"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/journals/cphysics/ArbeyMR19"}
    - slot{"paper_authors":"Alexandre Arbey"}
    - action_ask_for_link
* affirm
    - action_show_link
    - action_ask_for_authors
* affirm
    - action_show_authors
* paper_search{"paper_type":"gradient descent"}
    - slot{"paper_type":"gradient descent"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/journals/js/kjfnvkf"}
    - slot{"paper_authors":"jh  kjnkdf"}
    - action_ask_for_authors
* deny
    - utter_deny
* send_link
    - action_show_link

## Story
* paper_search
  - utter_what_type
* paper_category{"paper_type":"particle physics"}
  - slot{"paper_type":"particle physics"}
  - action_paper_search
  - slot{"paper_links":"https://dblp.org/rec/journals/adsv/dsf"}
  - slot{"paper_authors":"fvdgv  dfvdf"}
  - action_ask_for_link
* deny
  - utter_deny
* paper_search{"paper_type":"aerodynamics"}
    - slot{"paper_type":"aerodynamics"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKVsdcd"}
    - slot{"paper_authors":"sdcfdjknk jn"}
    - action_ask_for_link
* affirm
    - action_show_link
* send_authors
    - action_show_authors

## Story
* paper_search{"paper_type":"thermodynamics"}
    - slot{"paper_type":"thermodynamics"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/journals/adsv/dsf"}
    - slot{"paper_authors":"fvdgv  dfvdf"}
* send_link
    - action_show_link
* send_authors
    - action_show_authors
* paper_search{"paper_type":"aerodynamics"}
    - slot{"paper_type":"aerodynamics"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKVsdcd"}
    - slot{"paper_authors":"sdcfdjknk jn"}
    - action_ask_for_link
* deny
    - utter_deny

## Story
* paper_search
  - utter_what_type
* paper_category{"paper_type":"statistics"}
    - slot{"paper_type":"statistics"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/svfdvf"}
    - slot{"paper_authors":"sdcfdjknk jn"}
    - action_ask_for_link
* affirm+send_authors
  - action_show_link
  - action_show_authors
* paper_search{"paper_type":"linear regression"}
    - slot{"paper_type":"linear regression"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/journals/adsv/dsfdfre"}
    - slot{"paper_authors":"fvdgv  dfvdf"}
    - action_ask_for_link
* affirm
    - action_show_link
* send_authors
    - action_show_authors
* paper_search{"paper_type":"aerodynamics"}
    - slot{"paper_type":"aerodynamics"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKVsdcd"}
    - slot{"paper_authors":"sdcfdjknk jn"}
    - action_ask_for_link
* deny
    - utter_deny

## Story
* greet
  - utter_greet
* paper_search+send_authors{"paper_type":"geography"}
    - slot{"paper_type":"geography"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Frank Hutter"}
    - action_show_authors
    - action_ask_for_link
* affirm
  - action_show_link
* paper_search+send_authors+send_link{"paper_type":"history of the universe"}
    - slot{"paper_type":"history of the universe"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Frank Hutter"}
    - action_show_authors
    - action_show_link
* goodbye
    - utter_goodbye

## Story
* paper_search+send_link{"paper_type":"support vector machines"}
    - slot{"paper_type":"support vector machines"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Frank Hutter"}
    - action_show_link
    - action_show_authors

## Story
* greet
  - utter_greet
* paper_search{"paper_type":"mathematics"}
    - slot{"paper_type":"mathematics"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Frank Hutter"}
* send_authors
  - action_show_authors
  - action_ask_for_link
* affirm
  - action_show_link
* goodbye
  -utter_goodbye

## Story
* greet
  - utter_greet
* paper_search{"paper_type":"naive bayes"}
    - slot{"paper_type":"naive bayes"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Frank Hutter"}
* send_authors
  - action_show_authors
  - action_ask_for_link
* deny
  - utter_deny
* goodbye
  -utter_goodbye

## Story
* greet
  - utter_greet
* paper_search
  - utter_what_type
* paper_category{"paper_type":"learning"}
    - slot{"paper_type":"learning"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Frank Hutter"}
    - action_ask_for_authors
* affirm
  - action_show_authors

## Story
* greet
  - utter_greet
* paper_search
  - utter_what_type
* paper_category{"paper_type":"apriori algorithm"}
    - slot{"paper_type":"apriori algorithm"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Frank Hutter"}
    - action_ask_for_authors
* deny
  - utter_deny
* send_link
    - action_show_link

## Story
* greet
  - utter_greet
* paper_search+send_authors+send_link{"paper_type":"fibonacci heaps"}
    - slot{"paper_type":"fibonacci heaps"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Frank Hutter"}
    - action_show_authors
    - action_show_link
* paper_search+send_authors{"paper_type":"greedy algorithms"}
    - slot{"paper_type":"greedy algorithms"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Frank Hutter"}
    - action_show_authors
    - action_ask_for_link
* affirm
  - action_show_link
* paper_search+send_link{"paper_type":"red black trees"}
    - slot{"paper_type":"red black trees"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":"Frank Hutter"}
    - action_show_link
    - action_ask_for_authors
* deny
    - utter_deny
* goodbye
    - utter_goodbye

## Story
* greet
    - utter_greet
* paper_search{"paper_type":"machine learning"}
    - slot{"paper_type":"machine learning"}
    - action_paper_search
    - slot{"paper_links":"https://dblp.org/rec/books/sp/HKV2019"}
    - slot{"paper_authors":["Frank Hutter","Lars Kotthoff","Joaquin Vanschoren"]}
    - action_ask_for_authors
* affirm
    - action_show_authors
    - action_ask_for_link
* deny
    - utter_deny

## Story
* paper_search{"paper_type":"machine learning"}
    - slot{"paper_type":"machine learning"}
    - action_paper_search
    - slot{"counter":"0"}
    - slot{"paper_titles":["Automated Machine Learning - Methods, Systems, Challenges","Lifelong Machine Learning, Second Edition","Adversarial Machine Learning","Learning with Support Vector Machines","Advanced Lectures on Machine Learning, Machine Learning Summer School 2002, Canberra, Australia, February 11-22, 2002, Revised Lectures"]}
    - slot{"paper_links":["https://dblp.org/rec/books/sp/HKV2019","https://dblp.org/rec/series/synthesis/2018Chen","https://dblp.org/rec/series/synthesis/2018Vorobeychik","https://dblp.org/rec/series/synthesis/2011Campbell","https://dblp.org/rec/conf/mlss/2002"]}
    - slot{"paper_authors":["Frank Hutter;Lars Kotthoff;Joaquin Vanschoren","Zhiyuan Chen 0001;Bing Liu 0001","Yevgeniy Vorobeychik;Murat Kantarcioglu","Colin Campbell;Yiming Ying","Shahar Mendelson;Alexander J. Smola"]}
    - slot{"paper_years":["2019","2018","2018","2011","2003"]}
    - slot{"paper_pages":["Not known","Not known","Not known","Not known","Not known"]}
    - slot{"total_papers":"23384"}
* send_authors
    - action_show_authors
* send_link
    - action_show_link
* show_more_papers
    - action_show_more_papers
    - slot{"counter":"1"}
    - slot{"paper_titles":["Automated Machine Learning - Methods, Systems, Challenges","Lifelong Machine Learning, Second Edition","Adversarial Machine Learning","Learning with Support Vector Machines","Advanced Lectures on Machine Learning, Machine Learning Summer School 2002, Canberra, Australia, February 11-22, 2002, Revised Lectures"]}
    - slot{"paper_links":["https://dblp.org/rec/books/sp/HKV2019","https://dblp.org/rec/series/synthesis/2018Chen","https://dblp.org/rec/series/synthesis/2018Vorobeychik","https://dblp.org/rec/series/synthesis/2011Campbell","https://dblp.org/rec/conf/mlss/2002"]}
    - slot{"paper_authors":["Frank Hutter;Lars Kotthoff;Joaquin Vanschoren","Zhiyuan Chen 0001;Bing Liu 0001","Yevgeniy Vorobeychik;Murat Kantarcioglu","Colin Campbell;Yiming Ying","Shahar Mendelson;Alexander J. Smola"]}
    - slot{"paper_years":["2019","2018","2018","2011","2003"]}
    - slot{"paper_pages":["Not known","Not known","Not known","Not known","Not known"]}
* send_authors
    - action_show_authors
* show_more_papers
    - action_show_more_papers
    - slot{"counter":"2"}
    - slot{"paper_titles":["Automated Machine Learning - Methods, Systems, Challenges","Lifelong Machine Learning, Second Edition","Adversarial Machine Learning","Learning with Support Vector Machines","Advanced Lectures on Machine Learning, Machine Learning Summer School 2002, Canberra, Australia, February 11-22, 2002, Revised Lectures"]}
    - slot{"paper_links":["https://dblp.org/rec/books/sp/HKV2019","https://dblp.org/rec/series/synthesis/2018Chen","https://dblp.org/rec/series/synthesis/2018Vorobeychik","https://dblp.org/rec/series/synthesis/2011Campbell","https://dblp.org/rec/conf/mlss/2002"]}
    - slot{"paper_authors":["Frank Hutter;Lars Kotthoff;Joaquin Vanschoren","Zhiyuan Chen 0001;Bing Liu 0001","Yevgeniy Vorobeychik;Murat Kantarcioglu","Colin Campbell;Yiming Ying","Shahar Mendelson;Alexander J. Smola"]}
    - slot{"paper_years":["2019","2018","2018","2011","2003"]}
    - slot{"paper_pages":["Not known","Not known","Not known","Not known","Not known"]}
* send_authors+send_link
    - action_show_authors
    - action_show_link

## Story
* paper_search+send_authors{"paper_type":"greedy algorithms"}
    - slot{"paper_type":"greedy algorithms"}
    - action_paper_search
    - action_show_authors
    - action_ask_for_link
* affirm
  - action_show_link

## Story
* paper_search+send_year{"paper_type":"greedy algorithms"}
    - slot{"paper_type":"greedy algorithms"}
    - action_paper_search
    - action_show_year
    - action_ask_for_link
* affirm
  - action_show_link

## Story
* paper_search+send_pages{"paper_type":"greedy algorithms"}
    - slot{"paper_type":"greedy algorithms"}
    - action_paper_search
    - action_show_pages
    - action_ask_for_link
* affirm
  - action_show_link

## Story
* paper_search+send_authors{"paper_type":"greedy algorithms"}
    - slot{"paper_type":"greedy algorithms"}
    - action_paper_search
    - action_show_authors
    - action_ask_for_link
* affirm
  - action_show_link

## Story
* paper_search+send_link{"paper_type":"greedy algorithms"}
    - slot{"paper_type":"greedy algorithms"}
    - action_paper_search
    - action_show_link

## Story
* paper_search+send_year{"paper_type":"greedy algorithms"}
    - slot{"paper_type":"greedy algorithms"}
    - action_paper_search
    - action_show_year

## Story
* paper_search+send_pages{"paper_type":"greedy algorithms"}
    - slot{"paper_type":"greedy algorithms"}
    - action_paper_search
    - action_show_pages

## Story
* paper_search+send_authors+send_link{"paper_type":"greedy algorithms"}
    - slot{"paper_type":"greedy algorithms"}
    - action_paper_search
    - action_show_authors
    - action_show_link

## Story
* paper_search+send_authors+send_year{"paper_type":"greedy algorithms"}
    - slot{"paper_type":"greedy algorithms"}
    - action_paper_search
    - action_show_authors
    - action_show_year

## Story
* paper_search+send_authors+send_pages{"paper_type":"greedy algorithms"}
    - slot{"paper_type":"greedy algorithms"}
    - action_paper_search
    - action_show_authors
    - action_show_pages

## Story
* paper_search+send_year+send_pages{"paper_type":"greedy algorithms"}
    - slot{"paper_type":"greedy algorithms"}
    - action_paper_search
    - action_show_pages
    - action_show_year

## Story
* paper_search+send_authors+send_year+send_pages{"paper_type":"greedy algorithms"}
    - slot{"paper_type":"greedy algorithms"}
    - action_paper_search
    - action_show_authors
    - action_show_year
    - action_show_pages

## Story
* paper_search{"paper_type":"machine learning"}
    - slot{"paper_type":"machine learning"}
    - action_paper_search
* send_authors+send_link
    - action_show_authors
    - action_show_link

## Story
* paper_search{"paper_type":"machine learning"}
    - slot{"paper_type":"machine learning"}
    - action_paper_search
* send_authors+send_year
    - action_show_authors
    - action_show_year

## Story
* paper_search{"paper_type":"machine learning"}
    - slot{"paper_type":"machine learning"}
    - action_paper_search
* send_authors+send_pages
    - action_show_authors
    - action_show_pages

## Story
* paper_search{"paper_type":"machine learning"}
    - slot{"paper_type":"machine learning"}
    - action_paper_search
* send_year+send_pages
    - action_show_year
    - action_show_pages

## Story
* paper_search{"paper_type":"machine learning"}
    - slot{"paper_type":"machine learning"}
    - action_paper_search
* send_authors+send_pages+send_year
    - action_show_authors
    - action_show_year
    - action_show_pages

## Story
* paper_search{"paper_type":"machine learning"}
    - slot{"paper_type":"machine learning"}
    - action_paper_search
* send_paper_domain
    - action_show_paper_domain

## Story
* paper_search{"paper_type":"machine learning"}
    - slot{"paper_type":"machine learning"}
    - action_paper_search
* send_all
    - action_show_all

## Story
* paper_search+send_all{"paper_type":"machine learning"}
    - slot{"paper_type":"machine learning"}
    - action_show_all

## Story
* paper_search{"paper_type":"machine learning"}
    - slot{"paper_type":"machine learning"}
    - action_paper_search
* send_all
    - action_show_all
* send_stats
    - action_make_stats
    - utter_show_stats

## Story
* paper_search{"paper_type":"machine learning"}
    - slot{"paper_type":"machine learning"}
    - action_paper_search
* send_stats
    - action_make_stats
    - utter_show_stats