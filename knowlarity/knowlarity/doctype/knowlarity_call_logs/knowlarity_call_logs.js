// Copyright (c) 2023, Abhishek Chougule and contributors
// For license information, please see license.txt

frappe.ui.form.on('Knowlarity Call Logs', {
	download: function(frm) {
		if(frm.doc.call_recording)
		{
			window.open(frm.doc.call_recording, '_blank');
		}
	}
});
