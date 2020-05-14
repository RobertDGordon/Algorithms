#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = 0
  potential = []
  if len(ingredients) < len(recipe): #Add base case
    print('\nNot enough ingredients!\n')
    return 0
  for iKey, iVal in ingredients.items():
    for rKey, rVal in recipe.items():
      # print(f'recip: {rKey}-{rVal} ingre: {iKey}-{iVal}')
      if rKey == iKey:
        print(f'Checking {rKey}, required {rVal}, have {iVal}')
        if iVal < rVal:
          print(f'\n!Required {rKey} {rVal}, Only have {iKey} {iVal}')
          return 0
        # batches += 1 #can make at least one batch
        # if rVal * 2 < iVal:
          # print(f'Required {rKey} {rVal}, have double, {iKey} {iVal}')
        how_many = iVal // rVal
        print(f'{iKey}:{iVal} goes into {rVal}, {how_many} times')
        potential.append(how_many)
  batches = min(potential)
  print(f'\nPotential {batches} out of list {potential}\n')
  return batches      

# recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 })
# recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 10, 'sugar': 120, 'butter': 500 })
# recipe_batches({ 'milk': 2 }, { 'milk': 200})

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))