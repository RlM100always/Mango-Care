from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=255)
    brief_description = models.TextField()
    detailed_description = models.TextField()
    symptoms = models.JSONField(default=list)  # Store list of symptoms as JSON (works with SQLite)
    treatment = models.TextField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name



# diseases_list = [
#     Disease(
#         1,
#         "Anthracnose",
#         "A fungal disease affecting mango fruits and leaves",
#         "Anthracnose is a fungal disease caused by Colletotrichum gloeosporioides that affects all aerial parts of mango trees. It's particularly damaging during periods of high humidity and can significantly impact fruit quality and yield.",
#         [
#             "Small dark spots that enlarge into irregular brown-black lesions",
#             "Black or brown spots on flower panicles",
#             "Dark, sunken spots during ripening",
#             "Pinkish-orange spore masses on rotted areas",
#             "Leaf tissue may crack and fall out"
#         ],
#         "Preventive fungicide sprays are key. Use protectant fungicides (e.g. mancozeb or copper) from flowering until harvest. Maintain orchard hygiene by removing diseased panicles, mummified fruit, and dead twigs. Improve airflow through pruning and avoid overhead irrigation.",
#         "https://th.bing.com/th/id/OIP.1AXGSJftTnt4nlX-vp6QMQHaFi?rs=1&pid=ImgDetMain"
#     ),
#     Disease(
#         2,
#         "Bacterial Black Spot",
#         "A bacterial disease causing distinctive dark lesions",
#         "Bacterial black spot is caused by Xanthomonas campestris pv. mangiferaeindicae. It's particularly problematic in areas with high rainfall or where trees suffer injuries.",
#         [
#             "Irregular black spots with yellow halos on leaves",
#             "Black, cracked lesions on twigs and branches",
#             "Small, pitted black spots with star-shaped cracks on fruit",
#             "Tip dieback",
#             "Defoliation"
#         ],
#         "Use copper-based fungicide/bactericide sprays during growth flushes. Maintain orchard hygiene through pruning and destroying infected tissue. Implement practices to prevent wounds and reduce leaf wetness. Consider planting resistant varieties.",
#         "https://th.bing.com/th/id/OIP.nlxAzRdp8fklYElkf7jP_wHaE1?w=306&h=200&c=7&r=0&o=5&dpr=1.4&pid=1.7"
#     ),
#     Disease(
#         3,
#         "Mango Malformation Disease (MMD)",
#         "A fungal disease causing deformed growth of flowers and shoots",
#         "MMD is caused by various Fusarium species and disrupts hormonal balance. First detected in Australia in 2007, it is one of the major floral diseases of mango worldwide.",
#         [
#             "Compact, thickened flower panicles",
#             "Excessive, often sterile flowers",
#             "Misshapen shoot buds",
#             "Short internodes",
#             "Small, brittle, curling leaves"
#         ],
#         "Remove malformed inflorescences and shoots. Protect pruning wounds with fungicide paints or copper sprays. Use certified disease-free plants and consider removing highly susceptible cultivars.",
#         "https://www.industry.mangoes.net.au/~mangoesnet/cmsb/uploads/mango-malformation-disease-3.jpg"
#     ),
#     Disease(
#         4,
#         "Mango Scab",
#         "A fungal disease causing rough, scabby lesions",
#         "Mango scab is caused by Elsinoë mangiferae and is more common in coastal humid areas. First observed in Australia in the late 1990s, it affects leaves, fruit, and twigs.",
#         [
#             "Small, dark brown spots on leaves",
#             "Raised, corky scabs on fruit",
#             "Oval, grayish-white lesions on young twigs",
#             "Leaf distortion and crinkling",
#             "Multiple lesions causing fruit deformation"
#         ],
#         "Apply preventative copper-based or mancozeb sprays during flowering and fruit set. Improve airflow through pruning, avoid overhead irrigation, and remove infected material.",
#         "https://www.shutterstock.com/image-photo/this-symptoms-mango-scab-disease-260nw-2335461321.jpg"
#     ),
#     Disease(
#         5,
#         "Mango Seed Weevil",
#         "A fruit-infesting beetle affecting mango seeds",
#         "The mango seed weevil lays eggs in developing mangoes, with larvae burrowing into the fruit and damaging the seed. External damage often goes unnoticed.",
#         [
#             "Tiny holes or blemishes on fruit skin",
#             "Oozing sap from entry points",
#             "Hollowed out seeds",
#             "Larval tissue in seeds",
#             "Internal fruit damage"
#         ],
#         "Prevent movement of potentially infested fruit. Collect and destroy fallen fruit. Use timed insecticide applications to target adult weevils before egg laying.",
# "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSS3JtdEXjG_33iZVZK7dqZ58whgiIyC2ZtA&s"
#     ),
#     Disease(
#         6,
#         "Red Banded Mango Caterpillar",
#         "An insect pest that bores into mango fruits",
#         "The red banded mango caterpillar (RBMC) is an exotic threat capable of causing serious damage to mango crops through direct fruit boring.",
#         [
#             "Sap oozing from entry holes",
#             "Dark frass around entry points",
#             "Internal fruit tunneling",
#             "Wet rot development",
#             "Premature fruit drop"
#         ],
#         "Maintain strict fruit movement controls. Remove infested fruit and debris. Implement targeted insecticide sprays and utilize pheromone traps. Encourage natural enemies like parasitoid wasps.",
#         "https://apps.lucidcentral.org/pppw_v11/images/entities/mango_redbanded_caterpillar_281/stains.jpg"
#     ),
#     Disease(
#         7,
#         "Mango Gall Midge",
#         "Tiny flies causing gall formation on mango tissues",
#         "Mango gall midges are small flies whose larvae cause galls on mango leaves, flowers, and shoots. In Australia, the mango leaf gall midge is mainly found in northern regions.",
#         [
#             "Small reddish spots on new leaves",
#             "Wart-like formations",
#             "Twisted or curled leaves",
#             "Exit holes from larvae",
#             "Defoliation in severe cases"
#         ],
#         "Implement quarantine measures. Regularly inspect new growth for red spots or galls. Remove affected leaves and destroy heavily infested fallen leaves. Apply insecticides timed with new flushes.",
#         "https://th.bing.com/th/id/OIP.posBkTL7dwRzpdXmvYBr-QHaFb?rs=1&pid=ImgDetMain"
#     ),
# ]