from __future__ import absolute_import

import random
import requests
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from matplotlib import pyplot as plt


def fill_slots(response, paper_titles, paper_links, paper_authors,
               paper_years, paper_pages, paper_domain):    
    
    hits = response['result']['hits']['hit']
    for hit in hits:
        paper_titles.append(hit['info']['title'])
        paper_links.append(hit['info']['url'])
        paper_years.append(hit['info']['year'])
        paper_domain.append(hit['info']['type'])

        if 'pages' in hit['info'].keys():
            paper_pages.append(hit['info']['pages'])
        else:
            paper_pages.append('Not known')

        authors = hit['info']['authors']['author']
        if isinstance(authors, list): 
            paper_authors.append(';'.join(authors))
        else:
            paper_authors.append(authors)


class ActionPaperSearch(Action):
    
    def name(self):
        return "action_paper_search"

    def run(self, dispatcher, tracker, domain):
        
        paper_type = tracker.get_slot('paper_type')
        if not paper_type:
            dispatcher.utter_message("Unable to parse paper category:( \n.\n Enter paper type")
            return []

        response = requests.get('http://dblp.org/search/publ/api?q={}&format=json&h=5'.format(paper_type)).json()
        total_papers = response['result']['hits']['@total']
        
        if total_papers == '0':
            dispatcher.utter_message('No paper found:(')
            dispatcher.utter_message('Check the spelling once')
            return

        dispatcher.utter_message('There are total {} papers related to {}'.format(total_papers, paper_type))
        dispatcher.utter_message('Here is one of them')

        paper_titles, paper_links, paper_authors = [], [], []
        paper_years, paper_pages, paper_domain = [], [], []
        
        fill_slots(response, paper_titles, paper_links, paper_authors, paper_years, paper_pages, paper_domain)
        dispatcher.utter_message(paper_titles[0])

        return [
                    SlotSet('counter', '0'),
                    SlotSet('paper_titles', paper_titles),
                    SlotSet("paper_links", paper_links),
                    SlotSet("paper_authors", paper_authors),
                    SlotSet('paper_years', paper_years),
                    SlotSet('paper_pages', paper_pages),
                    SlotSet('paper_domain', paper_domain),
                    SlotSet('total_papers', total_papers)
                ]


class ActionShowMorePapers(Action):

    def name(self):
        return 'action_show_more_papers'

    def run(self, dispatcher, tracker, domain):
        
        paper_type = tracker.get_slot('paper_type')
        if not paper_type:
            dispatcher.utter_message("First enter category of paper you want to read")
            return

        total_papers = tracker.get_slot('total_papers')
        index = int(tracker.get_slot('counter')) + 1
        
        if int(total_papers) == index:
            dispatcher.utter_message('I have shown you all {} papers\n.\nNo more papers available:('.format(total_papers))
            return 

        paper_titles = tracker.get_slot('paper_titles')
       
        if index < len(paper_titles):
            dispatcher.utter_message(paper_titles[index])
            return [SlotSet('counter', str(index))]
        else:
            dispatcher.utter_message('fetching more papers...')
            response = requests.get('http://dblp.org/search/publ/api?q={}&format=json&h={}'.format(paper_type, index+5)).json()
            
            paper_titles, paper_links, paper_authors = [], [], []
            paper_years, paper_pages, paper_domain = [], [], []
            
            fill_slots(response, paper_titles, paper_links, paper_authors, paper_years, paper_pages, paper_domain)
            dispatcher.utter_message(paper_titles[index])

            return [
                        SlotSet('counter', str(index)),
                        SlotSet('paper_titles', paper_titles),
                        SlotSet('paper_links', paper_links),
                        SlotSet('paper_authors', paper_authors),
                        SlotSet('paper_years', paper_years),
                        SlotSet('paper_pages', paper_pages),
                        SlotSet('paper_domain', paper_domain)
                    ]


class ActionShowLink(Action):

    def name(self):
        return 'action_show_link'

    def run(self, dispatcher, tracker, domain):
        paper_type = tracker.get_slot('paper_type')
        if not paper_type:
            dispatcher.utter_message("No Paper found")
        
        counter = tracker.get_slot('counter')
        paper_links = tracker.get_slot('paper_links')
        dispatcher.utter_message('Here is a link to the paper - \n{}'.format(paper_links[int(counter)]))
        
        return 


class ActionShowYear(Action):

    def name(self):
        return 'action_show_year'

    def run(self, dispatcher, tracker, domain):
        paper_type = tracker.get_slot('paper_type')
        if not paper_type:
            dispatcher.utter_message("No Paper found")
        
        counter = tracker.get_slot('counter')
        paper_years = tracker.get_slot('paper_years')
        dispatcher.utter_message('Year of publication - {}'.format(paper_years[int(counter)]))
        
        return 


class ActionShowPages(Action):

    def name(self):
        return 'action_show_pages'

    def run(self, dispatcher, tracker, domain):
        paper_type = tracker.get_slot('paper_type')
        if not paper_type:
            dispatcher.utter_message("No Paper found")
        
        counter = tracker.get_slot('counter')
        paper_pages = tracker.get_slot('paper_pages')
        dispatcher.utter_message('Number of pages {}'.format(paper_pages[int(counter)]))
        
        return 


class ActionShowPaperDomain(Action):

    def name(self):
        return 'action_show_paper_domain'

    def run(self, dispatcher, tracker, domain):
        paper_type = tracker.get_slot('paper_type')
        if not paper_type:
            dispatcher.utter_message("No Paper found")
        
        counter = tracker.get_slot('counter')
        paper_domain = tracker.get_slot('paper_domain')
        dispatcher.utter_message(paper_domain[int(counter)])
        
        return 


class ActionShowAuthors(Action):

    def name(self):
        return 'action_show_authors'

    def run(self, dispatcher, tracker, domain):
        paper_type = tracker.get_slot('paper_type')
        if not paper_type:
            dispatcher.utter_message("No Paper found")
            return []

        counter = tracker.get_slot('counter')
        paper_authors = tracker.get_slot('paper_authors')
        
        reply = 'Authors of this paper -'

        authors = paper_authors[int(counter)].split(';')
        for author in authors:
            reply += '\n * {}'.format(author)

        dispatcher.utter_message(reply)
        return


class ActionShowAll(Action):

    def name(self):
        return 'action_show_all'

    def run(self, dispatcher, tracker, domain):
        paper_type = tracker.get_slot('paper_type')
        if not paper_type:
            dispatcher.utter_message("No Paper found")
        
        cur_index = int(tracker.get_slot('counter'))
        paper_domain = tracker.get_slot('paper_domain')
        paper_titles = tracker.get_slot('paper_titles')
        paper_years = tracker.get_slot('paper_years')
        paper_pages = tracker.get_slot('paper_pages')
        paper_authors = tracker.get_slot('paper_authors')
        paper_links = tracker.get_slot('paper_links')

        reply = '{} -\n'.format(paper_domain[cur_index])      
        reply += paper_titles[cur_index]
        reply += '\n.\nYear of release - {}'.format(paper_years[cur_index])
        reply += '\nTotal pages {}'.format(paper_pages[cur_index])

        dispatcher.utter_message(reply)

        reply = 'Authors of this paper -'

        authors = paper_authors[cur_index].split(';')
        for author in authors:
            reply += '\n * {}'.format(author)

        dispatcher.utter_message(reply)
        dispatcher.utter_message('Here is a link to the paper - \n{}'.format(paper_links[cur_index]))

        return 


class ActionMakeStats(Action):

    def name(self):
        return 'action_make_stats'

    def run(self, dispatcher, tracker, domain):
        paper_domain = tracker.get_slot('paper_domain')

        domain_count = {}
        for domain in paper_domain:
            if domain in domain_count.keys():
                domain_count[domain] += 1
            else:
                domain_count[domain] = 1

        counts = list(domain_count.values()) 
        explode = [0] * len(counts)
        explode[counts.index(max(counts))] = 0.1

        plt.pie(
            x = counts,
            labels = list(domain_count.keys()),
            explode = explode,
            autopct='%.2f%%',
            shadow = True,
            startangle = 90
            )
        plt.savefig('stat.png')
        plt.close()

        return [SlotSet('image_loc', 'stat.png')]


class ActionAskForLink(Action):

    def name(self):
        return 'action_ask_for_link'

    def run(self, dispatcher, tracker, domain):
        paper_type = tracker.get_slot('paper_type')

        if paper_type:

            template = [
                'Would you like to read this paper? I can send you a link.',
                'I would like to send link to this paper. Should I?',
                'Should I send a link?',
                'I can also send link to this paper. Would you like me to send?'
            ]

            dispatcher.utter_message(random.choice(template))

        return 


class ActionAskForAuthors(Action):

    def name(self):
        return 'action_ask_for_authors'

    def run(self, dispatcher, tracker, domain):
        paper_type = tracker.get_slot('paper_type')

        if paper_type:

            template = [
                'I can also show the authors. Would you like me to do that?',
                'Should I send the authors?',
                'Do you want to see the authors of this paper?'
                ]

            dispatcher.utter_message(random.choice(template))

        return 


# class ActionByePosFeed(Action):

#     def name(self):
#         return 'action_bye_posfeed'

#     def run(self, dispatcher, tracker, domain):
#         dispatcher.utter_template('utter_pos_feedback', tracker)
#         dispatcher.utter_template('utter_goodbye', tracker)

#         return


# class ActionByeAbuse(Action):

#     def name(self):
#         return 'action_bye_abuse'

#     def run(self, dispatcher, tracker, domain):
#         dispatcher.utter_template('utter_abuse', tracker)
#         dispatcher.utter_message('bye, have a nice day.')

#         return