Remove-Item '.\Introduction to Python (EN).zip', '.\Introduction to Python (GR).zip'
Compress-Archive -Path '.\Introduction to Python (EN).pdf', '.\code examples' -DestinationPath '.\Introduction to Python (EN).zip'
Compress-Archive -Path '.\Introduction to Python (GR).pdf', '.\code examples' -DestinationPath '.\Introduction to Python (GR).zip'
Remove-Item '.\Introduction to Python (EN).pdf', '.\Introduction to Python (GR).pdf'