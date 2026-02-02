class FilterAgent:
    def apply_filters(self, jobs, location=None, paid_only=None):
        filtered = jobs

        if location:
            filtered = [
                job for job in filtered
                if location.lower() in job["location"].lower()
            ]

        if paid_only is not None:
            filtered = [
                job for job in filtered
                if job["paid"] == paid_only
            ]

        return filtered
