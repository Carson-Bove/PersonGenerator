import random
import json
import os
def get_random_list():
   
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, 'population_stats.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        data_dict = json.load(f)
    population_list = []
    for country_name, stats in data_dict.items(): 
        obj = {"Country": country_name}
        obj.update(stats)
        population_list.append(obj)
    random.shuffle(population_list)

    return population_list

def simulate_person(): 
    seed = random.randint(0, 8056505564)
    gender_seed = random.randint(1,1000)
    sex = "female"
    country_list = get_random_list()
    gen_country = None
    countdown = seed
    for country in country_list:
        pop = country.get('Total Population (thousands)', 0) * 1000

        countdown -= pop

        if countdown < 0:
            gen_country = country
    gen_country_pop = gen_country.get('Total Population (thousands)', 0) * 1000
    gen_country_male_rate = int(round(( gen_country.get("Male Population (thousands)") * 1000 ) / gen_country_pop, 3) * 1000)
    gen_country_age_male = int(gen_country.get('Male Life Expectancy (years)', 0))
    gen_country_age_female = int(gen_country.get('Female Life Expectancy (years)', 0))
    gen_country_name = gen_country["Country"]
    if gender_seed < gen_country_male_rate:
        sex = "male"
        age = random.randint(0, gen_country_age_male)
    else:
        age = random.randint(0, gen_country_age_female)
    print(f"Simulated Person Is a {sex} {age} year old from {gen_country_name}")

simulate_person()
