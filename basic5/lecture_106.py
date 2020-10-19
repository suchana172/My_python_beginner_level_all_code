#import an entire module

import lecture_100
my_bw_ereader = lecture_100.Ereader('amazon','paperwhite','adjustable backlight ','several month of battery life','3000*800')
print(my_bw_ereader.get_ereader_name())
my_color_ereader = lecture_100.KindleFire('amazon','kindle fire','color screen','12 hours battery life','1280*800')
print(my_color_ereader.get_ereader_name())