from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def index(request):
    return render(request, 'main_page/index.html')

def hate(request):
    # add to hate table
    print('hating')
    return render(request, 'main_page/index.html')

def love(request):
    # add to love table
    print('loving')
    return render(request, 'main_page/index.html')



def list(request):
    return render(request, 'listings/index.html')


# def listing(self):
#     queue = Products.objects.raw(
#         'SELECT * FROM Products WHERE ProductID NOT IN (SELECT ProductID FROM Like WHERE user == logedUser)'
#         '                             AND ProductID NOT IN (SELECT ProductID FROM Hate WHERE user == loggedUser);')


def messages(request):
    messages = [
        MessageAsDisplayed(True, 'as;dflkasdf', datetime.datetime.now(), True),
        MessageAsDisplayed(True, 'askleg', datetime.datetime.now(), False),
        MessageAsDisplayed(True, 'as;ashevajsheg', datetime.datetime.now(), False),
    ]
    otherUser = {
        'username' : 'otherrrr.userrr',
        'picture' : 'https://i.imgur.com/Ss75Vfa.jpg'
    }
    messages_dict = {'messages' : messages, 'otherUser' : otherUser}
    return render(request, 'messages/index.html', context=messages_dict)


def new_list(request):
    return render(request, 'new_listings/index.html')


def profile(request):
    listings = [
        Listing('My stupid cat', 3.0, 'Fargo', 'https://i.imgur.com/Ss75Vfa.jpg'),
        Listing('My stupid dogs', 6.0, 'Bismarck', 'https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'),
        Listing('My stupid phone', 9.0, 'Grand Forks', 'https://scx1.b-cdn.net/csz/news/800/2015/howwilldatar.jpg'),
        Listing('My stupid cow Betsy', 12.0, 'Minneapolis', 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSYW0XEqHljEUNvoFfmEEpM7Z4cyq5V66MNrLyXerInvBFM5KUc&usqp=CAU'),
        Listing('My stupid used car', 16.50, 'Jamestown', 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ4B2mpOFXbAnsupjbRiAUambtV6jhyb4lx0sJuZOvp-s-VKjUS&usqp=CAU'),
        Listing('My stupid grandma', 300.0, 'Los Angeles', 'https://peoplescience.maritz.com/-/media/Maritz/Project/PeopleScience/Articles/adult-grandma-elderly-432722.ashx?h=900&w=1200&la=en&hash=5F66C65B032FEE90B10A489D08EC8B7D0E64B8CE'),
        Listing('My stupid science teacher', 34.0, 'Germany', 'https://pbs.twimg.com/profile_images/879355674957926400/VSGZHGib_400x400.jpg')
    ]
    listing_dict = {'listings' : listings}
    return render(request, 'profile/index.html', context=listing_dict)





class Listing:
    def __init__(self, title, price, city, imageUrl):
        self.title = title
        self.price = price
        self.city = city
        self.imageUrl = imageUrl

class MessageAsDisplayed:
    def __init__(self, recieved, messageBody, sentDate, needsDateSeparator):
        self.recieved = recieved
        self.messageBody = messageBody
        self.sentDate = sentDate
        self.needsDateSeparator = needsDateSeparator

class User:
    def __init__(self, id, username, location, pictureUrl, listings):
        self.id = id
        self.username = username
        self.location = location
        self.pictureUrl = pictureUrl
        self.listing = listings



users = [
    User(0, 'terry.crews', 'Fargo, ND', 'https://i.imgur.com/Ss75Vfa.jpg', []),
    User(1, 'some.user', 'Fargo, ND', 'https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',  []),
    User(2, 'someother.user', 'Fargo, ND', 'https://scx1.b-cdn.net/csz/news/800/2015/howwilldatar.jpg',  []),
    User(3, 'random.person21', 'Fargo, ND', 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSYW0XEqHljEUNvoFfmEEpM7Z4cyq5V66MNrLyXerInvBFM5KUc&usqp=CAU',  []),
    User(4, 'kanye.west', 'Fargo, ND', 'https://peoplescience.maritz.com/-/media/Maritz/Project/PeopleScience/Articles/adult-grandma-elderly-432722.ashx?h=900&w=1200&la=en&hash=5F66C65B032FEE90B10A489D08EC8B7D0E64B8CE',  []),
    User(5, 'kungfu.kenny', 'Fargo, ND', 'https://pbs.twimg.com/profile_images/879355674957926400/VSGZHGib_400x400.jpg', []),
    User(6, 'woah.kenny', 'Fargo, ND', 'https://i.imgur.com/Ss75Vfa.jpg', []),
]
