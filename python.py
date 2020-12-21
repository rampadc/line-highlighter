# Line 163 / productpage.py
def getForwardHeaders(request):
  headers = {}

  span = get_current_span()
  carrier = {}
  tracer.inject(
    span_context=span.context,
    format=Format.HTTP_HEADERS,
    carrier=carrier)
  headers.update(carrier)

  if 'user' in session:
    headers['end-user'] = session['user']
  # [... more code]
  return headers
