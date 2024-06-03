import math

def main():

    #textures_list = ["grained", "porphyroid", "porphyritic", "vesicular"]
    igneous_dict = {
        #rock: [mafic min %, mafic max %, quartz min %, quartz max %, feldspar min %, feldespar max %, type, texture]
        "rhyolite": [5, 50, 5, 100, 50, 100, "volcanic", "porphyritic"],
        "granite": [5, 50, 5, 100, 50, 100, "plutonic", ["grained", "porphyroid"]],
        "rhyodacite": [5, 50, 5, 100, 10, 50, "volcanic", "porphyritic"],
        "granodiorite": [5, 50, 5, 100, 10, 50, "plutonic", "grained"],
        "dacite": [5, 50, 5, 100, 0, 10, "volcanic", "porphyritic"],
        "tonalite": [5, 50, 5, 100, 0, 10, "plutonic", "grained"],
        "trachyte": [5, 50, 0, 5, 90, 100, "volcanic", "porphyritic"],
        "syenite": [5, 50, 0, 5, 90, 100, "plutonic", "grained"],
        "andesite": [5, 50, 0, 5, 0, 10, "volcanic", "porphyritic"],
        "diorite": [5, 50, 0, 5, 0, 10, "plutonic", "grained"],
        "basalt": [50, 100, 0, 5, 0, 10, "volcanic", "vesicular"],
        "gabbro": [50, 100, 0, 5, 0, 10, "plutonic", "grained"]

    }

    MAFIC_MIN_INDEX = 0
    MAFIC_MAX_INDEX = 1
    QUARTZ_MIN_INDEX = 2
    QUARTZ_MAX_INDEX = 3
    FELDESPAR_MIN_INDEX = 4
    FELDESPAR_MAX_INDEX = 5
    ROCK_TYPE_INDEX = 6
    TEXTURE_INDEX = 7
   
    print("Welcome to the rock identifier!")
    print("Please enter the percentages you observe in the sample (remember that the sum of these should not exceed 100).")
    print("NOTE: If the percentages indicate that your rock is an ANDESITE, DIORITE, BASALT or GABBRO finish determining the rock by the amount of plagioclase in your sample, use the colour of the sample as a determining factor.")

    while True:
    
        mafic_quantity = float(input("Enter the percentage of mafic minerals you observe: "))
        quartz_quantity = float(input("Enter the percentage of quartz you observe: "))
        feldespar_quantity = float(input("Enter the percentage of feldspar you observe: "))
        plagioclase_quantity = float(input("Enter the percentage of plagioclase you observe: "))
        texture = input("Enter the texture that best applies to your sample (grained, porphyroid, porphyritic or vesicular): ")

        total_percentage = mafic_quantity + quartz_quantity + feldespar_quantity + plagioclase_quantity
        if total_percentage <= 100:

            mafic_average = mafic_minerals_average(mafic_quantity, quartz_quantity, feldespar_quantity)
            quartz_average = quartz_mineral_average(quartz_quantity, feldespar_quantity, plagioclase_quantity)
            feldespar_average = alkali_feldespar_average(feldespar_quantity, plagioclase_quantity)

            print(f"Average of mafic minerals: {mafic_average:.2f}") 
            print(f"Quartz average: {quartz_average:.2f}") 
            print(f"Average feldspar: {feldespar_average:.2f}") 
    
            found_rocks = False
            for rock, range in igneous_dict.items():
        
                if (range[MAFIC_MIN_INDEX] <= mafic_average <= range[MAFIC_MAX_INDEX] and
                    range[QUARTZ_MIN_INDEX] <= quartz_average <= range[QUARTZ_MAX_INDEX] and
                    range[FELDESPAR_MIN_INDEX] <= feldespar_average <= range[FELDESPAR_MAX_INDEX] and 
                    texture in range[TEXTURE_INDEX]):
            
                    print("The identified rock is a:", rock, "and is of the type:", range[ROCK_TYPE_INDEX])
                    found_rocks = True
                    return  
                
            if not found_rocks:
                print("The rock could not be determined with the reported averages/texture.")
            return
        else:
            print("The sum of the percentages should not exceed 100%. Please try again.")    


def mafic_minerals_average(mafic_quantity, quartz_quantity, feldespar_quantity):

    mafic_average = (mafic_quantity / (mafic_quantity + quartz_quantity + feldespar_quantity)) * 100

    return mafic_average

def quartz_mineral_average(quartz_quantity, feldespar_quantity, plagioclase_quantity):
    
    quartz_average = (quartz_quantity / (quartz_quantity + (feldespar_quantity + plagioclase_quantity))) * 100

    return quartz_average

def alkali_feldespar_average(feldespar_quantity, plagioclase_quantity):

    feldespar_average = (feldespar_quantity / (feldespar_quantity + plagioclase_quantity)) * 100

    return feldespar_average

if __name__ == "__main__":
    main()