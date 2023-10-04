from datetime import date, datetime


def main():
    # write your code here
    today = date.today()
    print(today)
    
    now = datetime.now()
    print(now)
    
    d = today.strftime('%d/%m/%Y')
    print(d)

    d = now.strftime('%d/%m/%Y %H:%M')
    print(d)

    #print('Timezone:', now.tzinfo)
    timezone = now.astimezone()
    print('Timezone:', timezone.tzinfo)




    return

if __name__ == '__main__':
    main()