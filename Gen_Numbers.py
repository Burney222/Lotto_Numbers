import pandas as pd
import numpy as np

#Normal numbers
numbers_n_weights = np.array([(35,	0.788),
                            (30,	0.893),
                            (2	,1.003),
                            (24,	1.118),
                            (15,	0.790),
                            (48,	0.893),
                            (16,	1.006),
                            (4	,1.126),
                            (46,	0.808),
                            (28,	0.894),
                            (13,	1.037),
                            (25,	1.126),
                            (43,	0.834),
                            (47,	0.900),
                            (38,	1.041),
                            (32,	1.142),
                            (44,	0.842),
                            (21,	0.906),
                            (49,	1.044),
                            (19,	1.149),
                            (36,	0.848),
                            (1	,0.912	),
                            (18,	1.049),
                            (6	,1.162),
                            (45,	0.854),
                            (40,	0.915),
                            (23,	1.051),
                            (17,	1.164),
                            (29,	0.863),
                            (34,	0.925),
                            (27,	1.083),
                            (10,	1.170),
                            (14,	0.868),
                            (37,	0.938),
                            (31,	1.083),
                            (5	,1.193),
                            (22,	0.870),
                            (39,	0.985),
                            (26,	1.091),
                            (3	,1.210),
                            (20,	0.871),
                            (8	,0.991	),
                            (33,	1.100),
                            (9	,1.268),
                            (42,	0.885),
                            (41,	0.995),
                            (12,	1.110),
                            (11,	1.277),
                            (7	,1.291)], dtype=[("Number", "int"), ("Weight", "float")])
numbers_n_weights = np.sort(numbers_n_weights, 0)

numbers_n_weights = pd.DataFrame(numbers_n_weights, index=[numbers_n_weights["Number"]])
numbers_n_weights["Weight"] = 1/numbers_n_weights["Weight"]**2
numbers_n_weights["Probability"] = numbers_n_weights["Weight"]/np.sum(numbers_n_weights["Weight"])

lotto_numbers = np.random.choice(numbers_n_weights["Number"], size=6, replace=True)

#Super Number
super_numbers_n_weights = np.array([(0,	0.783),
                                    (1,	0.878),
                                    (2,	0.934),
                                    (9,	0.949),
                                    (4,	0.980),
                                    (6,	1.030),
                                    (3,	1.062),
                                    (8,	1.073),
                                    (5,	1.146),
                                    (7,	1.151)], dtype=[("Number", "int"), ("Weight", "float")])
super_numbers_n_weights = np.sort(super_numbers_n_weights, 0)
super_numbers_n_weights = pd.DataFrame(super_numbers_n_weights, index=[super_numbers_n_weights["Number"]])
super_numbers_n_weights["Weight"] = 1/super_numbers_n_weights["Weight"]**2

#Was number drawn in normal numbers?
for lotto_number in lotto_numbers:
    super_numbers_n_weights = super_numbers_n_weights[super_numbers_n_weights["Number"] != lotto_number]

super_numbers_n_weights["Probability"] = super_numbers_n_weights["Weight"]/np.sum(super_numbers_n_weights["Weight"])
super_number = np.random.choice(super_numbers_n_weights["Number"])

print("Lotto numbers/super number: {}/{}".format(lotto_numbers, super_number))
