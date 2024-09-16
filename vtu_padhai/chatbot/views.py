from django.http import JsonResponse
from django.shortcuts import render

# Define chatbot responses
def get_chatbot_response(user_message):
    response_dict = {
        'hello': 'Hello! How can I assist you with VTU Padhai today?',
        'hi': 'Hi! What can I help you with?',
        'how are you': 'I am just a bot, but I am here to help you with VTU queries!',
        'courses': 'We offer various courses like B.E, B.Tech, M.Tech, MBA, and MCA. Which one would you like to know more about?',
        'exam schedule': 'The next VTU exam schedule will be released soon. Stay tuned!',
        'fees': 'The tuition fees depend on the course. Please provide more details about your course.',
        'syllabus': 'You can access the VTU syllabus online. Would you like me to guide you there?',
        'admission': 'Admissions are open for various courses. Please check the VTU website for eligibility criteria and deadlines.',
        'results': 'Results are usually declared a few weeks after the exams. You can check them on the official VTU site.',
        'time table': 'The semester timetable is available on the VTU portal. Do you need help navigating there?',
        'contact': 'You can reach the VTU helpdesk at helpdesk@vtu.ac.in.',
        'support': 'For technical issues, contact support at techsupport@vtu.ac.in.',
        'branches': 'We offer engineering branches like CSE, ECE, EEE, Mechanical, and Civil. Which branch are you interested in?',
        'attendance': 'Attendance regulations require at least 75%. Please ensure you comply to avoid issues.',
        'placements': 'Our placement cell partners with top companies for campus recruitment. Are you looking for placement statistics?',
        'library': 'The VTU library is well-equipped with resources. You can access digital materials through the VTU online portal.',
        'scholarships': 'VTU offers merit-based and need-based scholarships. Do you want more information on eligibility?',
        'internships': 'We encourage students to apply for internships through the placement cell.',
        'hostel': 'VTU has hostel facilities for both boys and girls. Contact the administration for availability and fees.',
        'grading': 'The grading system is CGPA-based. Need help understanding the grading criteria?',
        'lab': 'Lab facilities are available for various branches. Ensure you book slots in advance.',
        'events': 'There are several technical and cultural events held throughout the year. Stay updated via the VTU event calendar.',
        'tech fest': 'Our next tech fest is coming soon! You can participate in various competitions and workshops.',
        'about vtu': 'VTU is one of the largest technological universities in India. It provides excellent academic resources and infrastructure.',
        'default': "I'm sorry, I don't understand that. Can you ask something else?",
        'creators':"S Uday Kiran and Koustav Biswas"
    }

    # Ensure the user input is processed in lowercase to match dictionary keys
    user_message_lower = user_message.lower()
    return response_dict.get(user_message_lower, response_dict['default'])


# Handle chatbot messages
def chatbot(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        response_message = get_chatbot_response(user_message)
        return JsonResponse({'response': response_message})


# Render the chatbot interface
def chatbot_interface(request):
    return render(request, 'chatbot.html')
