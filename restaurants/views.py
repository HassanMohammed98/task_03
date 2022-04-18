from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        'my_list':[
            {
                'restaurant_name':"Freej Swaelah",
                'food_type':"Arabic",
            },
            {
                'restaurant_name':"Johnny Rockets",
                'food_type':"American",
            },
            {
                'restaurant_name':"DOH",
                'food_type':"Desserts",
            },
        ],
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        'my_object':
        {
            'restaurant_name':"DOH",
            'food_type':"Desserts",
        },
    }
    return render(request, 'detail.html', context)
