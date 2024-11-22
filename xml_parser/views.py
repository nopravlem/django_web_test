from django import forms, shortcuts
import xml.etree.ElementTree as ET 

class XMLUploadForm(forms.Form):
    xml_file = forms.FileField()

def parse_XML_file(request):
    if request.method == 'POST':
        form = XMLUploadForm(request.POST, request.FILES)
        if form.is_valid():
            xml_file = request.FILES['xml_file']
            # Parse the XML data
            root = ET.parse(xml_file).getroot()

            # Process the XML data as needed
            # ...

            return shortcuts.render(request, 'upload_success.html')
    else:
        form = XMLUploadForm()
    return shortcuts.render(request, 'form.html', {'form': form})
