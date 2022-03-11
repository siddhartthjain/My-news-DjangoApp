from django.db.models import fields
from django.http.response import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from .forms import commentform, post_form
from django.shortcuts import redirect, render
from django.urls.base import reverse, reverse_lazy
from django.views.generic import CreateView,ListView
from .models import ask_question, post,comments,review
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages



# Create your views here.
def main(request):
    return render(request,'home/front.html')

class create(LoginRequiredMixin,CreateView):
    model=post
    fields=['title','post_image','caption']
    # fields='__all__'
    template_name='home/createpost.html'
    # context_object_name='form'
    success_url=reverse_lazy('all')

    def get(self, request, pk=None):
        form = post_form()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)


    def post(self,request):
        form=post_form(request.POST,request.FILES )
        
        if not form.is_valid():
            cntx={'form':form}
            return render(request,self.template_name,cntx)
        else:
            post=form.save(commit=False)
            post.owner=self.request.user
            post.save()
            return redirect(self.success_url)   


class all(ListView):
    model=post
    template_name='home/list.html'
    context_object_name="posts"
    ordering=['-created']

class update(LoginRequiredMixin,UpdateView):
    model=post
    template_name='home/createpost.html'
    success_url=reverse_lazy('main')
    fields=["title",'post_image','caption']

class delete(LoginRequiredMixin,DeleteView):
    model=post
    template_name='home/confirm_delete.html'
    context_object_name='post'
    success_url=reverse_lazy('main')

class forum_create(CreateView):
    model=ask_question
    template_name='home/forum_create.html'
    fields=['question']
    success_url=reverse_lazy('forum') 



class forum(ListView):
    model=ask_question
    template_name='home/forums.html'
    context_object_name="forums"



class forum_detail( DetailView):
    model=ask_question
    def get(self,request,pk):
        question=ask_question.objects.get(id=pk)
        form=commentform()
        comment=comments.objects.filter(com_ques=question)
        cntx={'question':question,'form':form,'comments':comment }

        return render(request,'home/forum_detail.html',cntx)



          

class create_comment(LoginRequiredMixin,View):
    def post(self,request,pk):
        ques=ask_question.objects.get(id=pk)
        com=comments(com=request.POST['com'],user=request.user,com_ques=ques)
        com.save()
        return redirect(reverse('forum_detail',args=[pk]))


class forum_comment_delete(LoginRequiredMixin,DeleteView):
    model=comments
    template_name='home/confirm_delete.html'
    
    def get_success_url(self):
        ques=self.object.com_ques
        return reverse('forum_detail',args=[ques.id])
    

class forum_delete(DeleteView):
    model=ask_question
    template_name='home/confirm_delete.html'
    success_url=reverse_lazy('forum')    

class give_review(CreateView):
    model=review
    template_name='home/review.html'
    fields='__all__'
    success_url=reverse_lazy('review')
     
    


        



        

