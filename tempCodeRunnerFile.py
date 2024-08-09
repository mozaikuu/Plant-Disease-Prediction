
        if isplant(img) == False:
            skip = False
            print("no plant detected")
            # print("stuck1")
            # sys.exit() #make it wait 5 seconds and try again
        else:
            print("Plant detected")
            # print("stuck2")
            first_run = False
            skip = True
    
    if skip:
        result_index = predict_disease(img)
        model_prediction = class_names[result_index]
        print("Predicted Disease:", model_prediction)
        # print("stuck3")
        
        
        if count % 300 == 0:
                # if "healthy" in model_prediction.lower():
                #     count = 299
                # else:        
                    prep_and_send_email(model_prediction, soil_moisture_sensor_Email())
                    count = 0
                    # print("stuck5")
                    
        count += 1
        print(count)
        # print("stuck6")
        
        
        # myData()
    else:
        time.sleep(5)
        # print("stuck7")