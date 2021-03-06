#
# id/iso scale factors
#

# idIsoScaleFactors = {}

#
#    First two columns are Eta range.
#    Next 2 columns are PT range.
#    Column 5 & 6 shows the efficiency in data and statistical error.
#    Column 7 & 8 shows the efficiency in MC and statistical error.
#    Column 9 shows the systematics uncertainty because of changing signal PDF.
#    Column 10 shows the systematics uncertainty because of changing background PDF.
#    Column 11 - systematics after changing the fit range.
#    Column 12 - systematics because of NLO and LO MC sample.
#    Last two columns will be systematics because of Tag selection and PU reweighing. But their effect will be really small.
#    


idIsoScaleFactors['mu'] = [
      #
      #     Data                                                                                                   MC
      # etamin  etamax            ptmin   ptmax         eff     deff_high       deff_low                                     eff     deff_high       deff_low
      #
      ((  -2.4  ,  -2.1  ),   (  10  ,    12  ),   (  0.609191   ,     0.0505912    ,    0.046392      )      ,    (      0.662717    ,    0.0318054    ,    0.0310346    )  ),
      ((  -2.1  ,  -1.6  ),   (  10  ,    12  ),   (  0.694852   ,     0.0411551    ,    0.038435      )      ,    (      0.739247    ,    0.0250985    ,    0.0246161    )  ),
      ((  -1.6  ,  -1.2  ),   (  10  ,    12  ),   (  0.755197   ,     0.0570244    ,    0.0515263     )      ,    (      0.717399    ,    0.0292931    ,    0.0285201    )  ),
      ((  -1.2  ,  -0.8  ),   (  10  ,    12  ),   (  0.63816    ,     0.0482268    ,    0.0444536     )      ,    (      0.64859     ,    0.0350546    ,    0.0337255    )  ),
      ((  -0.8  ,  -0.3  ),   (  10  ,    12  ),   (  0.643485   ,     0.0758017    ,    0.0656495     )      ,    (      0.70171     ,    0.0580256    ,    0.0528833    )  ),
      ((  -0.3  ,  0.3   ),   (  10  ,    12  ),   (  0.793632   ,     0.206368     ,    0.140157      )      ,    (      0.59381     ,    0.124362     ,    0.0770163    )  ),
      ((  0.3   ,  0.8   ),   (  10  ,    12  ),   (  0.652629   ,     0.0768807    ,    0.06567       )      ,    (      0.629706    ,    0.0521628    ,    0.0479061    )  ),
      ((  0.8   ,  1.2   ),   (  10  ,    12  ),   (  0.613056   ,     0.0464505    ,    0.0427027     )      ,    (      0.692426    ,    0.0403409    ,    0.0382883    )  ),
      ((  1.2   ,  1.6   ),   (  10  ,    12  ),   (  0.671009   ,     0.0475424    ,    0.0436988     )      ,    (      0.743658    ,    0.0335523    ,    0.0327089    )  ),
      ((  1.6   ,  2.1   ),   (  10  ,    12  ),   (  0.702874   ,     0.0400315    ,    0.0374584     )      ,    (      0.738502    ,    0.0239133    ,    0.0237897    )  ),
      ((  2.1   ,  2.4   ),   (  10  ,    12  ),   (  0.570238   ,     0.0469337    ,    0.0431632     )      ,    (      0.583771    ,    0.0343286    ,    0.0332475    )  ),
      ((  -2.4  ,  -2.1  ),   (  12  ,    14  ),   (  0.711305   ,     0.0414417    ,    0.0457666     )      ,    (      0.699497    ,    0.0243827    ,    0.0243246    )  ),
      ((  -2.1  ,  -1.6  ),   (  12  ,    14  ),   (  0.75699    ,     0.0284811    ,    0.0275562     )      ,    (      0.759308    ,    0.0187099    ,    0.0186959    )  ),
      ((  -1.6  ,  -1.2  ),   (  12  ,    14  ),   (  0.81946    ,     0.0346971    ,    0.0333734     )      ,    (      0.780081    ,    0.0206678    ,    0.0205603    )  ),
      ((  -1.2  ,  -0.8  ),   (  12  ,    14  ),   (  0.679189   ,     0.031062     ,    0.0299151     )      ,    (      0.679641    ,    0.0220503    ,    0.0218176    )  ),
      ((  -0.8  ,  -0.3  ),   (  12  ,    14  ),   (  0.550219   ,     0.0360329    ,    0.0338887     )      ,    (      0.651697    ,    0.028405     ,    0.0277891    )  ),
      ((  -0.3  ,  0.3   ),   (  12  ,    14  ),   (  0.718381   ,     0.0638202    ,    0.0567939     )      ,    (      0.630792    ,    0.0369063    ,    0.0350965    )  ),
      ((  0.3   ,  0.8   ),   (  12  ,    14  ),   (  0.650339   ,     0.0469499    ,    0.0431441     )      ,    (      0.610031    ,    0.028289     ,    0.0276811    )  ),
      ((  0.8   ,  1.2   ),   (  12  ,    14  ),   (  0.72383    ,     0.0345435    ,    0.0331091     )      ,    (      0.698667    ,    0.023771     ,    0.0234192    )  ),
      ((  1.2   ,  1.6   ),   (  12  ,    14  ),   (  0.75767    ,     0.0327225    ,    0.0316022     )      ,    (      0.80939     ,    0.000950154  ,    0.000950154  )  ),
      ((  1.6   ,  2.1   ),   (  12  ,    14  ),   (  0.733869   ,     0.0269707    ,    0.0262032     )      ,    (      0.740157    ,    0.0180632    ,    0.0181374    )  ),
      ((  2.1   ,  2.4   ),   (  12  ,    14  ),   (  0.712851   ,     0.0366411    ,    0.0352244     )      ,    (      0.676252    ,    0.0261876    ,    0.0260587    )  ),
      ((  -2.4  ,  -2.1  ),   (  14  ,    16  ),   (  0.709302   ,     0.0275203    ,    0.026904      )      ,    (      0.709794    ,    0.0202471    ,    0.0201613    )  ),
      ((  -2.1  ,  -1.6  ),   (  14  ,    16  ),   (  0.782865   ,     0.0212928    ,    0.0211248     )      ,    (      0.780497    ,    0.0151103    ,    0.0152412    )  ),
      ((  -1.6  ,  -1.2  ),   (  14  ,    16  ),   (  0.789469   ,     0.0244601    ,    0.0241236     )      ,    (      0.767383    ,    0.0168666    ,    0.0170633    )  ),
      ((  -1.2  ,  -0.8  ),   (  14  ,    16  ),   (  0.757837   ,     0.0248238    ,    0.0243203     )      ,    (      0.728975    ,    0.00010819   ,    0.00010819   )  ),
      ((  -0.8  ,  -0.3  ),   (  14  ,    16  ),   (  0.706889   ,     0.0286876    ,    0.0277451     )      ,    (      0.700192    ,    0.0208452    ,    0.020837     )  ),
      ((  -0.3  ,  0.3   ),   (  14  ,    16  ),   (  0.611941   ,     0.0316454    ,    0.0301301     )      ,    (      0.668875    ,    0.0251619    ,    0.0245257    )  ),
      ((  0.3   ,  0.8   ),   (  14  ,    16  ),   (  0.730242   ,     0.0299967    ,    0.0289587     )      ,    (      0.733275    ,    0.020687     ,    0.0204854    )  ),
      ((  0.8   ,  1.2   ),   (  14  ,    16  ),   (  0.715513   ,     0.0243011    ,    0.0237222     )      ,    (      0.763898    ,    0.000905238  ,    0.000905238  )  ),
      ((  1.2   ,  1.6   ),   (  14  ,    16  ),   (  0.757097   ,     0.0238421    ,    0.0234511     )      ,    (      0.775733    ,    0.0166865    ,    0.016782     )  ),
      ((  1.6   ,  2.1   ),   (  14  ,    16  ),   (  0.797222   ,     0.0218466    ,    0.0215096     )      ,    (      0.794051    ,    0.015083     ,    0.015164     )  ),
      ((  2.1   ,  2.4   ),   (  14  ,    16  ),   (  0.70916    ,     0.0277918    ,    0.0271758     )      ,    (      0.737855    ,    0.0216941    ,    0.0217017    )  ),
      ((  -2.4  ,  -2.1  ),   (  16  ,    18  ),   (  0.719315   ,     0.0229293    ,    0.0226715     )      ,    (      0.765522    ,    0.0163573    ,    0.0165221    )  ),
      ((  -2.1  ,  -1.6  ),   (  16  ,    18  ),   (  0.854368   ,     0.0175277    ,    0.0175215     )      ,    (      0.805454    ,    0.0120124    ,    0.0121352    )  ),
      ((  -1.6  ,  -1.2  ),   (  16  ,    18  ),   (  0.796413   ,     0.0173691    ,    0.0173365     )      ,    (      0.843145    ,    0.0128143    ,    0.0129954    )  ),
      ((  -1.2  ,  -0.8  ),   (  16  ,    18  ),   (  0.764471   ,     0.0176001    ,    0.0175156     )      ,    (      0.788083    ,    0.0138631    ,    0.0139617    )  ),
      ((  -0.8  ,  -0.3  ),   (  16  ,    18  ),   (  0.698952   ,     0.0185104    ,    0.0183615     )      ,    (      0.754651    ,    0.0153764    ,    0.0152866    )  ),
      ((  -0.3  ,  0.3   ),   (  16  ,    18  ),   (  0.666964   ,     0.0220381    ,    0.0215216     )      ,    (      0.681576    ,    0.0172152    ,    0.0171627    )  ),
      ((  0.3   ,  0.8   ),   (  16  ,    18  ),   (  0.70076    ,     0.0190476    ,    0.0187956     )      ,    (       0.721073   ,     0.0144398   ,     0.0144456   )  ),
      ((  0.8   ,  1.2   ),   (  16  ,    18  ),   (  0.778511   ,     0.0185625    ,    0.0184745     )      ,    (      0.746027    ,    0.000714994  ,    0.000714994  )  ),
      ((  1.2   ,  1.6   ),   (  16  ,    18  ),   (  0.844304   ,     0.0183219    ,    0.0182963     )      ,    (      0.817279    ,    0.0130618    ,    0.0132132    )  ),
      ((  1.6   ,  2.1   ),   (  16  ,    18  ),   (  0.797473   ,     0.0155106    ,    0.0154888     )      ,    (      0.815348    ,    0.0120199    ,    0.0120199    )  ),
      ((  2.1   ,  2.4   ),   (  16  ,    18  ),   (  0.743389   ,     0.00127047   ,    0.00127047    )      ,    (      0.754093    ,    0.0173522    ,    0.0175692    )  ),
      ((  -2.4  ,  -2.1  ),   (  18  ,    20  ),   (  0.782952   ,     0.0177545    ,    0.0177176     )      ,    (      0.828203    ,    0.0128128    ,    0.0129268    )  ),
      ((  -2.1  ,  -1.6  ),   (  18  ,    20  ),   (  0.823157   ,     0.0132744    ,    0.0129056     )      ,    (      0.842691    ,    0.000545142  ,    0.000545142  )  ),
      ((  -1.6  ,  -1.2  ),   (  18  ,    20  ),   (  0.853531   ,     0.0135003    ,    0.0135504     )      ,    (      0.847778    ,    0.010076     ,    0.0102449    )  ),
      ((  -1.2  ,  -0.8  ),   (  18  ,    20  ),   (  0.795686   ,     0.00108047   ,    0.00108047    )      ,    (      0.809178    ,    0.0108778    ,    0.0110247    )  ),
      ((  -0.8  ,  -0.3  ),   (  18  ,    20  ),   (  0.781154   ,     0.0145993    ,    0.0145583     )      ,    (      0.799433    ,    0.0104602    ,    0.0105375    )  ),
      ((  -0.3  ,  0.3   ),   (  18  ,    20  ),   (  0.710272   ,     0.0162757    ,    0.0161014     )      ,    (      0.74812     ,    0.0120436    ,    0.0120844    )  ),
      ((  0.3   ,  0.8   ),   (  18  ,    20  ),   (  0.775584   ,     0.0137248    ,    0.0139581     )      ,    (      0.787318    ,    0.0109211    ,    0.0110005    )  ),
      ((  0.8   ,  1.2   ),   (  18  ,    20  ),   (  0.770218   ,     0.0141955    ,    0.0142102     )      ,    (      0.807485    ,    0.0111796    ,    0.0112741    )  ),
      ((  1.2   ,  1.6   ),   (  18  ,    20  ),   (  0.837214   ,     0.0137978    ,    0.0138312     )      ,    (      0.85252     ,    0.0103693    ,    0.0105043    )  ),
      ((  1.6   ,  2.1   ),   (  18  ,    20  ),   (  0.827776   ,     0.0121816    ,    0.0122558     )      ,    (      0.849128    ,    0.00952011   ,    0.00965207   )  ),
      ((  2.1   ,  2.4   ),   (  18  ,    20  ),   (  0.75266    ,     0.0181498    ,    0.0181813     )      ,    (      0.796896    ,    0.0129238    ,    0.013057     )  ),
      ((  -2.4  ,  -2.1  ),   (  20  ,    22  ),   (  0.825887   ,     0.014626     ,    0.0211193     )      ,    (      0.846914    ,    0.0104341    ,    0.0106126    )  ),
      ((  -2.1  ,  -1.6  ),   (  20  ,    22  ),   (  0.877446   ,     0.00993529   ,    0.0100439     )      ,    (      0.854671    ,    0.00739227   ,    0.00750066   )  ),
      ((  -1.6  ,  -1.2  ),   (  20  ,    22  ),   (  0.846839   ,     0.0109312    ,    0.0110313     )      ,    (      0.863061    ,    0.00799043   ,    0.00815068   )  ),
      ((  -1.2  ,  -0.8  ),   (  20  ,    22  ),   (  0.841294   ,     0.0109346    ,    0.0110659     )      ,    (      0.862633    ,    0.00827571   ,    0.00827571   )  ),
      ((  -0.8  ,  -0.3  ),   (  20  ,    22  ),   (  0.805234   ,     0.0102989    ,    0.0103103     )      ,    (      0.818477    ,    0.0079918    ,    0.00808404   )  ),
      ((  -0.3  ,  0.3   ),   (  20  ,    22  ),   (  0.780035   ,     0.0116156    ,    0.0115981     )      ,    (      0.785503    ,    0.00846162   ,    0.00852265   )  ),
      ((  0.3   ,  0.8   ),   (  20  ,    22  ),   (  0.80075    ,     0.0110476    ,    0.0110884     )      ,    (      0.817538    ,    0.00799558   ,    0.00807259   )  ),
      ((  0.8   ,  1.2   ),   (  20  ,    22  ),   (  0.844605   ,     0.0115695    ,    0.0116614     )      ,    (      0.850679    ,    0.00861833   ,    0.00874807   )  ),
      ((  1.2   ,  1.6   ),   (  20  ,    22  ),   (  0.856635   ,     0.0125646    ,    0.0107974     )      ,    (      0.864611    ,    0.00806349   ,    0.00818283   )  ),
      ((  1.6   ,  2.1   ),   (  20  ,    22  ),   (  0.841483   ,     0.00983061   ,    0.00994469    )      ,    (      0.872623    ,    0.00715989   ,    0.00730327   )  ),
      ((  2.1   ,  2.4   ),   (  20  ,    22  ),   (  0.807477   ,     0.0139516    ,    0.0140601     )      ,    (      0.843578    ,    0.010964     ,    0.01127      )  ),
      ((  -2.4  ,  -2.1  ),   (  22  ,    24  ),   (  0.835947   ,     0.0117898    ,    0.0119255     )      ,    (      0.842348    ,    0.00876985   ,    0.0090053    )  ),
      ((  -2.1  ,  -1.6  ),   (  22  ,    24  ),   (  0.873783   ,     0.00804896   ,    0.00819691    )      ,    (      0.891368    ,    0.00596031   ,    0.00606487   )  ),
      ((  -1.6  ,  -1.2  ),   (  22  ,    24  ),   (  0.889372   ,     0.00874421   ,    0.00886121    )      ,    (      0.904413    ,    0.00667006   ,    0.00679905   )  ),
      ((  -1.2  ,  -0.8  ),   (  22  ,    24  ),   (  0.862499   ,     0.00869574   ,    0.00880934    )      ,    (      0.881777    ,    0.00666764   ,    0.00677737   )  ),
      ((  -0.8  ,  -0.3  ),   (  22  ,    24  ),   (  0.835331   ,     0.00857072   ,    0.00866954    )      ,    (      0.847222    ,    0.00624112   ,    0.00631998   )  ),
      ((  -0.3  ,  0.3   ),   (  22  ,    24  ),   (  0.809229   ,     0.00819311   ,    0.0082229     )      ,    (      0.823957    ,    0.00605853   ,    0.00608868   )  ),
      ((  0.3   ,  0.8   ),   (  22  ,    24  ),   (  0.845825   ,     0.00820352   ,    0.00827445    )      ,    (      0.853198    ,    0.00621462   ,    0.00629099   )  ),
      ((  0.8   ,  1.2   ),   (  22  ,    24  ),   (  0.857275   ,     0.0088594    ,    0.00896709    )      ,    (      0.862751    ,    0.00722376   ,    0.00732415   )  ),
      ((  1.2   ,  1.6   ),   (  22  ,    24  ),   (  0.884176   ,     0.0088471    ,    0.00897135    )      ,    (      0.867339    ,    8.68008e-06  ,    8.68008e-06  )  ),
      ((  1.6   ,  2.1   ),   (  22  ,    24  ),   (  0.885313   ,     0.00790987   ,    0.00803464    )      ,    (      0.891453    ,    0.00599291   ,    0.0060966    )  ),
      ((  2.1   ,  2.4   ),   (  22  ,    24  ),   (  0.828625   ,     0.011846     ,    0.0120183     )      ,    (      0.84958     ,    0.00901678   ,    0.00918848   )  ),
      ((  -2.4  ,  -2.1  ),   (  24  ,    26  ),   (  0.853918   ,     0.0105695    ,    0.0107679     )      ,    (      0.870336    ,    0.00775852   ,    0.00792876   )  ),
      ((  -2.1  ,  -1.6  ),   (  24  ,    26  ),   (  0.885645   ,     0.00689143   ,    0.00699469    )      ,    (      0.912623    ,    0.004978     ,    0.00508892   )  ),
      ((  -1.6  ,  -1.2  ),   (  24  ,    26  ),   (  0.909142   ,     0.00703343   ,    0.00718785    )      ,    (      0.908322    ,    0.00580223   ,    0.00591767   )  ),
      ((  -1.2  ,  -0.8  ),   (  24  ,    26  ),   (  0.892147   ,     0.00727263   ,    0.007398      )      ,    (      0.87896     ,    0.00607531   ,    0.00618822   )  ),
      ((  -0.8  ,  -0.3  ),   (  24  ,    26  ),   (  0.853794   ,     0.0067163    ,    0.0067826     )      ,    (      0.86785     ,    0.00530949   ,    0.00537304   )  ),
      ((  -0.3  ,  0.3   ),   (  24  ,    26  ),   (  0.842573   ,     0.00628315   ,    0.00632814    )      ,    (      0.840187    ,    0.00466914   ,    0.00471456   )  ),
      ((  0.3   ,  0.8   ),   (  24  ,    26  ),   (  0.868025   ,     0.00658143   ,    0.00666467    )      ,    (      0.863446    ,    0.00518655   ,    0.00525091   )  ),
      ((  0.8   ,  1.2   ),   (  24  ,    26  ),   (  0.876987   ,     0.00757513   ,    0.00768269    )      ,    (      0.882837    ,    0.00607018   ,    0.0062014    )  ),
      ((  1.2   ,  1.6   ),   (  24  ,    26  ),   (  0.8939     ,     0.00723619   ,    0.0073691     )      ,    (      0.886565    ,    0.00594646   ,    0.00603955   )  ),
      ((  1.6   ,  2.1   ),   (  24  ,    26  ),   (  0.895945   ,     0.0066707    ,    0.00680145    )      ,    (      0.907484    ,    0.00516186   ,    0.00525975   )  ),
      ((  2.1   ,  2.4   ),   (  24  ,    26  ),   (  0.843579   ,     0.0102603    ,    0.0104021     )      ,    (      0.885132    ,    0.00754767   ,    0.00771672   )  ),
      ((  -2.4  ,  -2.1  ),   (  26  ,    30  ),   (  0.876984   ,     0.00623406   ,    0.00630964    )      ,    (      0.888472    ,    0.0045817    ,    0.00466037   )  ),
      ((  -2.1  ,  -1.6  ),   (  26  ,    30  ),   (  0.920229   ,     0.00378968   ,    0.00384143    )      ,    (      0.926736    ,    0.00290861   ,    0.00295132   )  ),
      ((  -1.6  ,  -1.2  ),   (  26  ,    30  ),   (  0.924062   ,     0.00404354   ,    0.00409984    )      ,    (      0.916797    ,    0.00340065   ,    0.00345275   )  ),
      ((  -1.2  ,  -0.8  ),   (  26  ,    30  ),   (  0.893534   ,     0.00426723   ,    0.00431047    )      ,    (      0.90509     ,    0.00338767   ,    0.00342684   )  ),
      ((  -0.8  ,  -0.3  ),   (  26  ,    30  ),   (  0.881438   ,     0.00364956   ,    0.00368079    )      ,    (      0.892732    ,    0.00285243   ,    0.00287413   )  ),
      ((  -0.3  ,  0.3   ),   (  26  ,    30  ),   (  0.868091   ,     0.00314166   ,    0.00316625    )      ,    (      0.882323    ,    0.00241515   ,    0.00243227   )  ),
      ((  0.3   ,  0.8   ),   (  26  ,    30  ),   (  0.889795   ,     0.00359029   ,    0.00362561    )      ,    (      0.898206    ,    0.00278933   ,    0.00281084   )  ),
      ((  0.8   ,  1.2   ),   (  26  ,    30  ),   (  0.89539    ,     0.00424388   ,    0.00428894    )      ,    (      0.902       ,    0.00338572   ,    0.00342911   )  ),
      ((  1.2   ,  1.6   ),   (  26  ,    30  ),   (  0.922084   ,     0.0041009    ,    0.00416732    )      ,    (      0.919259    ,    0.00338392   ,    0.00342202   )  ),
      ((  1.6   ,  2.1   ),   (  26  ,    30  ),   (  0.917397   ,     0.00379747   ,    0.00384988    )      ,    (      0.921664    ,    0.00297673   ,    0.00302491   )  ),
      ((  2.1   ,  2.4   ),   (  26  ,    30  ),   (  0.870336   ,     0.00616378   ,    0.00626097    )      ,    (      0.90068     ,    0.00443485   ,    0.00452487   )  ),
      ((  -2.4  ,  -2.1  ),   (  30  ,    35  ),   (  0.902932   ,     0.00440143   ,    0.0044528     )      ,    (      0.9217      ,    0.00312439   ,    0.00316137   )  ),
      ((  -2.1  ,  -1.6  ),   (  30  ,    35  ),   (  0.939126   ,     0.00254247   ,    0.00257612    )      ,    (      0.946843    ,    0.00198337   ,    0.00200987   )  ),
      ((  -1.6  ,  -1.2  ),   (  30  ,    35  ),   (  0.944519   ,     0.00266185   ,    0.00270133    )      ,    (      0.940061    ,    0.00223257   ,    0.00226764   )  ),
      ((  -1.2  ,  -0.8  ),   (  30  ,    35  ),   (  0.925906   ,     0.00267025   ,    0.00270476    )      ,    (      0.927727    ,    0.00223174   ,    0.00225506   )  ),
      ((  -0.8  ,  -0.3  ),   (  30  ,    35  ),   (  0.918285   ,     0.00214196   ,    0.00216677    )      ,    (      0.927432    ,    0.00171218   ,    0.00172879   )  ),
      ((  -0.3  ,  0.3   ),   (  30  ,    35  ),   (  0.905224   ,     0.0019522    ,    0.00196201    )      ,    (      0.907722    ,    0.00159539   ,    0.00160388   )  ),
      ((  0.3   ,  0.8   ),   (  30  ,    35  ),   (  0.918325   ,     0.00216144   ,    0.00218305    )      ,    (      0.922631    ,    0.00175048   ,    0.00177228   )  ),
      ((  0.8   ,  1.2   ),   (  30  ,    35  ),   (  0.9258     ,     0.00266355   ,    0.00268505    )      ,    (      0.923835    ,    0.00224381   ,    0.00226343   )  ),
      ((  1.2   ,  1.6   ),   (  30  ,    35  ),   (  0.941402   ,     0.00269591   ,    0.00272886    )      ,    (      0.939065    ,    0.00222738   ,    0.0022549    )  ),
      ((  1.6   ,  2.1   ),   (  30  ,    35  ),   (  0.938432   ,     0.00247926   ,    0.00251091    )      ,    (      0.947504    ,    0.00198487   ,    0.00201669   )  ),
      ((  2.1   ,  2.4   ),   (  30  ,    35  ),   (  0.892593   ,     0.00432646   ,    0.00437147    )      ,    (      0.917765    ,    0.00310213   ,    0.00315124   )  ),
      ((  -2.4  ,  -2.1  ),   (  35  ,    40  ),   (  0.915363   ,     0.00345937   ,    0.00350866    )      ,    (      0.948659    ,    0.00221878   ,    0.00225192   )  ),
      ((  -2.1  ,  -1.6  ),   (  35  ,    40  ),   (  0.956623   ,     0.00182254   ,    0.00185009    )      ,    (      0.963984    ,    0.00137468   ,    0.00139287   )  ),
      ((  -1.6  ,  -1.2  ),   (  35  ,    40  ),   (  0.959873   ,     0.00179237   ,    0.00182776    )      ,    (      0.958741    ,    0.00148642   ,    0.00151381   )  ),
      ((  -1.2  ,  -0.8  ),   (  35  ,    40  ),   (  0.944738   ,     0.00176347   ,    0.00178384    )      ,    (      0.949236    ,    0.00143781   ,    0.00145881   )  ),
      ((  -0.8  ,  -0.3  ),   (  35  ,    40  ),   (  0.94296    ,     0.00150057   ,    0.00151224    )      ,    (      0.946981    ,    0.00120283   ,    0.0012153    )  ),
      ((  -0.3  ,  0.3   ),   (  35  ,    40  ),   (  0.926415   ,     0.00148533   ,    0.00149636    )      ,    (      0.93568     ,    0.00118163   ,    0.00119115   )  ),
      ((  0.3   ,  0.8   ),   (  35  ,    40  ),   (  0.943697   ,     0.00146756   ,    0.00148918    )      ,    (      0.948124    ,    0.00120657   ,    0.00122688   )  ),
      ((  0.8   ,  1.2   ),   (  35  ,    40  ),   (  0.945693   ,     0.00180636   ,    0.00181167    )      ,    (      0.949322    ,    0.00144348   ,    0.00145938   )  ),
      ((  1.2   ,  1.6   ),   (  35  ,    40  ),   (  0.960788   ,     0.00176532   ,    0.00179857    )      ,    (      0.9598      ,    0.00147063   ,    0.00148932   )  ),
      ((  1.6   ,  2.1   ),   (  35  ,    40  ),   (  0.959814   ,     0.00173359   ,    0.00176363    )      ,    (      0.96081     ,    0.00144391   ,    0.00146398   )  ),
      ((  2.1   ,  2.4   ),   (  35  ,    40  ),   (  0.909034   ,     0.00341823   ,    0.00346528    )      ,    (      0.941866    ,    0.00234114   ,    0.00238161   )  ),
      ((  -2.4  ,  -2.1  ),   (  40  ,    60  ),   (  0.935168   ,     0.00192372   ,    0.00194728    )      ,    (      0.966849    ,    0.00113625   ,    0.00115503   )  ),
      ((  -2.1  ,  -1.6  ),   (  40  ,    60  ),   (  0.972728   ,     0.000854706  ,    0.000864708   )      ,    (      0.982903    ,    0.000550344  ,    0.000558478  )  ),
      ((  -1.6  ,  -1.2  ),   (  40  ,    60  ),   (  0.979032   ,     0.000743577  ,    0.000755307   )      ,    (      0.981572    ,    0.000580596  ,    0.000589959  )  ),
      ((  -1.2  ,  -0.8  ),   (  40  ,    60  ),   (  0.971767   ,     0.000778011  ,    0.000787399   )      ,    (      0.975316    ,    0.000618786  ,    0.00062682   )  ),
      ((  -0.8  ,  -0.3  ),   (  40  ,    60  ),   (  0.96594    ,     0.000733259  ,    0.000741459   )      ,    (      0.971927    ,    0.000578926  ,    0.000585226  )  ),
      ((  -0.3  ,  0.3   ),   (  40  ,    60  ),   (  0.952294   ,     0.000766726  ,    0.000772285   )      ,    (      0.961638    ,    0.000597189  ,    0.000601483  )  ),
      ((  0.3   ,  0.8   ),   (  40  ,    60  ),   (  0.968424   ,     0.000713724  ,    0.000718045   )      ,    (      0.972827    ,    0.000568891  ,    0.000570899  )  ),
      ((  0.8   ,  1.2   ),   (  40  ,    60  ),   (  0.96819    ,     0.000803304  ,    0.000814718   )      ,    (      0.975458    ,    0.000615366  ,    0.000623426  )  ),
      ((  1.2   ,  1.6   ),   (  40  ,    60  ),   (  0.978344   ,     0.000744728  ,    0.000755432   )      ,    (      0.980271    ,    0.000595273  ,    0.000602442  )  ),
      ((  1.6   ,  2.1   ),   (  40  ,    60  ),   (  0.975655   ,     0.000794055  ,    0.00080194    )      ,    (      0.982889    ,    0.000564245  ,    0.000564245  )  ),
      ((  2.1   ,  2.4   ),   (  40  ,    60  ),   (  0.938733   ,     0.00184374   ,    0.001859      )      ,    (      0.966883    ,    0.00113963   ,    0.00115799   )  ),
      ((  -2.4  ,  -2.1  ),   (  60  ,    100 ),   (  0.940227   ,     0.00731075   ,    0.00743026    )      ,    (      0.983932    ,    0.00367156   ,    0.00383573   )  ),
      ((  -2.1  ,  -1.6  ),   (  60  ,    100 ),   (  0.979226   ,     0.00328213   ,    0.00337669    )      ,    (      0.990645    ,    0.0017334    ,    0.00182136   )  ),
      ((  -1.6  ,  -1.2  ),   (  60  ,    100 ),   (  0.986672   ,     0.00262208   ,    0.00271604    )      ,    (      0.992742    ,    0.00166142   ,    0.0017523    )  ),
      ((  -1.2  ,  -0.8  ),   (  60  ,    100 ),   (  0.975382   ,     0.00256738   ,    0.00265173    )      ,    (      0.985177    ,    0.00170072   ,    0.00178228   )  ),
      ((  -0.8  ,  -0.3  ),   (  60  ,    100 ),   (  0.981391   ,     0.00216456   ,    0.00221417    )      ,    (      0.98692     ,    -0           ,    -0           )  ),
      ((  -0.3  ,  0.3   ),   (  60  ,    100 ),   (  0.970308   ,     0.00226593   ,    0.00231517    )      ,    (      0.976887    ,    0.00160764   ,    0.00165592   )  ),
      ((  0.3   ,  0.8   ),   (  60  ,    100 ),   (  0.979009   ,     0.00224209   ,    0.00229543    )      ,    (      0.987812    ,    0.00148428   ,    0.00154864   )  ),
      ((  0.8   ,  1.2   ),   (  60  ,    100 ),   (  0.974574   ,     0.00257239   ,    0.00266115    )      ,    (      0.985631    ,    0.00175732   ,    0.00175732   )  ),
      ((  1.2   ,  1.6   ),   (  60  ,    100 ),   (  0.989283   ,     0.002475     ,    0.0025835     )      ,    (      0.990739    ,    0.00168901   ,    0.00177782   )  ),
      ((  1.6   ,  2.1   ),   (  60  ,    100 ),   (  0.983286   ,     0.00287259   ,    0.00297549    )      ,    (      0.991092    ,    0.00161814   ,    0.00170073   )  ),
      ((  2.1   ,  2.4   ),   (  60  ,    100 ),   (  0.953555   ,     0.00665328   ,    0.00679875    )      ,    (      0.979918    ,    0.00349065   ,    0.00364892   )  ),
      ((  -2.4  ,  -2.1  ),   (  100 ,    200 ),   (  0.969605   ,     0.0303946    ,    0.0456895     )      ,    (      0.955833    ,    0.0144719    ,    0.0154512    )  ),
      ((  -2.1  ,  -1.6  ),   (  100 ,    200 ),   (  0.989647   ,     0.0103527    ,    0.0147399     )      ,    (      0.989915    ,    0.00648024   ,    0.00718811   )  ),
      ((  -1.6  ,  -1.2  ),   (  100 ,    200 ),   (  0.973115   ,     0.0121619    ,    0.0127334     )      ,    (      0.983634    ,    0.00609705   ,    0.0068728    )  ),
      ((  -1.2  ,  -0.8  ),   (  100 ,    200 ),   (  0.975677   ,     0.00856672   ,    0.00914916    )      ,    (      0.984984    ,    0.00541338   ,    0.00613235   )  ),
      ((  -0.8  ,  -0.3  ),   (  100 ,    200 ),   (  0.987107   ,     0.0070539    ,    0.00761957    )      ,    (      0.985671    ,    0.00535267   ,    0.00589363   )  ),
      ((  -0.3  ,  0.3   ),   (  100 ,    200 ),   (  0.982479   ,     0.00728964   ,    0.00771951    )      ,    (      0.980143    ,    0.00564371   ,    0.00610064   )  ),
      ((  0.3   ,  0.8   ),   (  100 ,    200 ),   (  0.981033   ,     0.00647612   ,    0.00695554    )      ,    (      0.985945    ,    0.00496525   ,    0.0054633    )  ),
      ((  0.8   ,  1.2   ),   (  100 ,    200 ),   (  0.965634   ,     0.00950398   ,    0.0100967     )      ,    (      0.981223    ,    0.00581905   ,    0.00645027   )  ),
      ((  1.2   ,  1.6   ),   (  100 ,    200 ),   (  0.98561    ,     0.0108281    ,    0.011596      )      ,    (      0.998923    ,    0.00107721   ,    0.0056031    )  ),
      ((  1.6   ,  2.1   ),   (  100 ,    200 ),   (  0.987623   ,     0.0112929    ,    0.0118445     )      ,    (      0.99897     ,    0.00102998   ,    0.00610916   )  ),
      ((  2.1   ,  2.4   ),   (  100 ,    200 ),   (  0.930516   ,     0.0354067    ,    0.0348806     )      ,    (      1           ,    1.13999e-08  ,    0.00896103   )  ),
     ]
   
   
                            

                                                                                                 
       
        
        
        