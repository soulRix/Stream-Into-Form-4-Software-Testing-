#################################################################################################
#                                       For Update Stream Package                               #  
#################################################################################################
        streamPackageName = request.form.getlist('streamName[]')
        subjectChoice = request.form.getlist('checkboxSubject')
        subjectChoice2 = request.form.getlist('checkboxSubject2')
        subjectChoice3 = request.form.getlist('checkboxSubject3')
        subjectChoice4 = request.form.getlist('checkboxSubject4')
        subjectChoice5 = request.form.getlist('checkboxSubject5')
        subjectChoice6 = request.form.getlist('checkboxSubject6')
        subjectChoice7 = request.form.getlist('checkboxSubject7')
        subjectChoice8 = request.form.getlist('checkboxSubject8')
        subjectChoice9 = request.form.getlist('checkboxSubject9')
        subjectChoice10 = request.form.getlist('checkboxSubject10')

        subjectChoiceBool = True
        subjectChoiceBool2 = True
        subjectChoiceBool3 = True
        subjectChoiceBool3 = True
        subjectChoiceBool4 = True
        subjectChoiceBool5 = True
        subjectChoiceBool6 = True
        subjectChoiceBool7 = True
        subjectChoiceBool8 = True
        subjectChoiceBool9 = True
        subjectChoiceBool10 = True

        newStreamName = []
        for index,valueName in enumerate(streamPackageName):
            if (not(valueName and not valueName.isspace())):
                continue
            newStreamName.append(valueName)

        oldStreamPackage =  len(school.stream_packages)
        sizeStreamName = len(newStreamName)

        for index,valueName in enumerate(newStreamName):
            if  index <= oldStreamPackage:
                if school.school_stream[index].stream_name != valueName:
                    school_stream[index].stream_name = valueName 
                elif school.school_stream[index].stream_name == newStreamName[index]: 
                    pass
            else:
                school.stream_packages.append(StreamPackage(stream_name = valueName))
            
            if subjectChoice and index <= oldStreamPackage and subjectChoiceBool:
                for indexSubject,valueSubject in enumerate(subjectChoice):
                    if (not(valueSubject and not valueSubject.isspace())):
                        continue
                    tempsize = school.stream_packages[index].subjects
                    if school.school_stream[index].subjects[indexSubject] == valueSubject:
                        pass
                    elif school.school_stream[index].subjects[indexSubject] != valueSubject:
                        search_subject = Subject.query.filter_by(subject_title = valueSubject).first()
            else:
                find_subject = Subject.query.filter_by(subject_title = valueSubject).first()
                school.stream_packages[index].subjects.append(find_subject)


        for index,valueName in enumerate(streamPackageName):
            
            if (not(valueName and not valueName.isspace())):
                # If One of the exists field is empty just delete the whole data
                #temp = school.stream_packages[index]
                temp = school_stream[index]
                if temp:
                    db.session.delete(temp)
                continue
            elif school_stream[index].stream_name == valueName:
                pass
            elif school_stream[index].stream_name != valueName:
                school_stream[index].stream_name = valueName       
            else:
                school.stream_packages.append(StreamPackage(stream_name = valueName))

            for index2,valueSubject in enumerate(subjectChoice):
                print(valueSubject)
                print(type(valueSubject))
                if (not(valueSubject and not valueSubject.isspace())):
                    # If One of the exists field is empty just delete the whole data
                    #temp2 = school.stream_packages[index].subjects[index2]
                    temp2 = school_stream[index].subjects[index2]
                    if temp2:
                        db.session.delete(temp2)
                    continue
                elif school_stream[index].subjects[index2].subject_title == valueSubject:
                    pass
                elif school_stream[index].subjects[index2].subject_title != valueSubject:
                    print(valueSubject)
                    find_subject = Subject.query.filter_by(subject_title = valueSubject).first()
                    school.streamPackageName[index].subjects[index2].id = find_subject.id
                else:
                    find_subject = Subject.query.filter_by(subject_title = valueSubject).first()
                    school.stream_packages[index].subjects.append(find_subject)

#################################################################################################
#                                                                                               #  
#################################################################################################



<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
<script>
    var xValues = ["4 Epic", "4 Good","4 Awesome", "4 Marvelous", "4 Legend", "4 Adorable"];
    var yValues = [35, 27, 20, 22, 30, 50];
    var barColors = ["red", "green","blue","orange","brown","cyan"];
    
    new Chart("studentClass", 
    {
      type: "bar",
      data: 
      {
        labels: xValues,
        datasets: 
        [{
            backgroundColor: barColors,
            data: yValues
        }]
      },
      options: 
      {
        scales:
        {
            xAxes: 
            [{
                time: {
                unit: 'month'
                },
                gridLines: {
                display: false
                },
                ticks: {
                maxTicksLimit: 6
                }
            }],
            yAxes: 
            [{
                ticks: {
                min: 0,
                max: 60,
                maxTicksLimit: 5
                },
                gridLines: {
                display: true
                }
            }],
        },   
        legend: {display: false},
        title: {
          display: true,
          text: "Student's per Class"
        }
      }
    });
</script>

















# 