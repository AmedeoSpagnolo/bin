
A = ["IDEO_music","LaughDetection","aero-debug.log","ai4r","airpollution","auto_layout","butterfly","chumchum","chumchum_app","dot_attraction_test","fracture","genki","iutils","kwan-portfolio","laravel-video-chat","lullababy","lullaby_website","ml","monarch_interactive","monarch_prototypes","p2pvc","pinky","pix2pix-tensorflow","prototype_shape_project_calendar","python-ps4","recovery codes","runway","ryokoyokota","tool-runway"]
B = ["AB_testing_T3","GoogleModelViewer-Allin","JasonRampe1_Attractor","MAKERSCHOOL01_react","NFT-Marker-Creator","SonyVerse1","UnityVrTemplates","aframe-hit-test","ai4r","airpollution","amt-wavenet","amt-wavenet_2","auto_layout","chumchum","codekit","darkchess","faceswap","figma_ext_01","figmapluginMusic","gemini_ar","genki","howler.js","ideo_1","illustrator_script","iot_nano_mesher","lullababy","monarch_prototypes","motoHide","mstp","origami-flask","parrot","particle-cli","pasty","plugin-samples","project_calendar","report.txt","runway","ryokoyokota","shimne","sonyverse","speech_recognition","squash","supper","tane","test01_figma-plugin","tool-runway","tree_Viz","turing-patterns-master.zip","website_template","wpa2-wordlists"]

only_A = []
only_B = []
A_and_B = []
B_and_A = []

for i in A:
    if i in B:
        A_and_B.append(i)
    else:
        only_A.append(i)

for i in B:
    if i not in A:
        only_B.append(i)

print "---"
print "A: "+ str(len(A)) + " elements"
print(", ".join(A))
print "---"
print "B: "+ str(len(B)) + " elements"
print(", ".join(B))
print "---"
print "Only A: " + str(len(only_A)) + " elements"
print(", ".join(only_A))
print "---"
print "Only B: " + str(len(only_B)) + " elements"
print(", ".join(only_B))
print "---"
print "A and B: " + str(len(A_and_B)) + " elements"
print(", ".join(A_and_B))
