from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')


# Create your views here.
def topics(request):
    """Show all topics."""
    all_topics = Topic.objects.order_by('date_added')
    context = {'topics': all_topics}
    return render(request, 'learning_logs/topics.html', context)


# Create your views here.
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    selected = Topic.objects.get(id=topic_id)
    entries = selected.entry_set.order_by('-date_added')
    context = {'topic': selected, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)

    if form.is_valid():
        form.save()
        return redirect('learning_logs:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Add a new entry."""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)

    if form.is_valid():
        entry = form.save(commit=False)
        entry.topic = topic
        entry.save()

        return redirect('learning_logs:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    """Add a new entry."""
    entry = Entry.objects.get(id=entry_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm(instance=entry)
    else:
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry, data=request.POST)

    if form.is_valid():
        entry.save()
        return redirect('learning_logs:topic', topic_id=entry.topic.id)

    # Display a blank or invalid form.
    context = {'entry': entry, 'topic': entry.topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
