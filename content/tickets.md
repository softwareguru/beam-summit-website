---
title: "Tickets"
date: 2022-02-14T13:51:25+06:00
description: "Get your tickets for Beam Summit 2022"

sitemap:
  priority: 0.9

---

## Ticket types and price

<table class="table prices">
<tr>
  <th>Ticket type</th>
  <th>Early bird price (May 13th 2022)</th>
  <th>Regular price</th>
</tr>
<tr>
  <td>Online attendance</td>
  <td>Free</td>
  <td>Free</td>
</tr>
<tr>
  <td>In-person attendance for July 18-19 (conference)</td>
  <td>$230</td>
  <td>$290</td>
</tr>
<tr>
  <td>In-person attendance for July 18-20 (conference & workshops)</td>
  <td>$290</td>
  <td>$350</td>
</tr>
</table>

<div class="d-flex justify-content-center mb-4">

<!-- Noscript content for added SEO -->
<noscript><a href="https://beamsummit-2022.eventbrite.com" rel="noopener noreferrer" target="_blank">Buy Tickets on Eventbrite</a></noscript>
<!-- You can customize this button any way you like -->
<button id="eventbrite-widget-modal-trigger-261321558817" type="button" class="btn btn-yellow btn-rounded mt-3">Get your tickets</button>

<script src="https://www.eventbrite.com/static/widgets/eb_widgets.js"></script>

<script type="text/javascript">

  function getGAClientID() {
    result = 0;
    var trackers = [];
    try {
      trackers = ga.getAll();
    } catch (error) {
      console.log("Could not load ga")
    }  
    var i, len;
    for (i = 0, len = trackers.length; i < len; i += 1) {
      if (trackers[i].get('trackingId') === 'UA-165970215-2') {
        result = trackers[i].get('clientId');
      }
    }
    console.log("Returning "+result);
    return result;
  }

  var exampleCallback = function() {
    console.log('Order complete!');
  };
  
    
  window.EBWidgets.createWidget({
    widgetType: 'checkout',
    eventId: '261321558817',
    googleAnalyticsClientId: getGAClientID(),
    modal: true,
    modalTriggerElementId: 'eventbrite-widget-modal-trigger-261321558817',
    onOrderComplete: exampleCallback
  });
</script>
</div>

## Apply for a scholarship


If you would like to attend in person but cannot afford a ticket, please <a href="https://forms.gle/STT1tYp9MefGzN5L9" target="_blank">apply for a scholarship.</a>


***Scholarship covers the conference pass only, not travel accommodations.***