from django.shortcuts import render,redirect
from .models import Skill, Blog,Contact,Projects

def profile(request):
    return render(request, 'profile.html')

def projects(request):
    # Lấy tất cả dự án từ database, sắp xếp theo thứ tự mới nhất (nếu có trường date)
    projects = Projects.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def skills(request):
    skills = Skill.objects.all()
    return render(request, 'skills.html', {'skills': skills})

def blogs(request):
    blogs = Blog.objects.all().order_by('-date_posted')
    return render(request, 'blogs.html', {'blogs': blogs})

def contact(request):
    if request.method == 'POST':
        ho_ten = request.POST.get('ho_ten', '').strip()
        email = request.POST.get('email', '').strip()
        tin_nhan = request.POST.get('tin_nhan', '').strip()
        sdt = request.POST.get('sdt', '').strip()

        if not ho_ten or not email or not tin_nhan:
            return render(request, 'contact.html', {
                'error': 'Vui lòng điền đầy đủ thông tin!'
            })

        if sdt and len(sdt) != 10:
            return render(request, 'contact.html', {
                'error': 'Số điện thoại phải có 10 chữ số, vui lòng nhập lại!'
            })

        Contact.objects.create(ho_ten=ho_ten, email=email, tin_nhan=tin_nhan, sdt=sdt)
        return redirect('/contact/?success=true')

    return render(request, 'contact.html')

def home(request):
    projects = Projects.objects.all() 
    # 2. Sửa đường dẫn template cho khớp với cấu trúc thư mục
    for project in projects:
        if project.tech_stack:
            project.tech_list = [tag.strip() for tag in project.tech_stack.split(',')]
        else:
            project.tech_list = []

    phrases = [
        'Kiến Tạo Tương Lai Tài Chính Số',
        'Sinh viên Công nghệ Tài chính',
        'Đam mê Phân tích Dữ liệu',
    ]
    
    return render(request, 'home.html', {
        'projects': projects,
        'phrases': phrases,
    })